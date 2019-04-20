#!/bin/bash
# Docker entrypoint script.

# Wait until Postgres is ready
while ! pg_isready -q -h $PGHOST -p $PGPORT -U $PGUSER
do
    echo "$(date) - waiting for database to start"
    sleep 2
done

# Create, migrate, and seed database if it doesn't exist.
if [[ -z `psql -Atqc "\\list $PGDATABASE"` ]]; then
    flask db init
    flask db migrate
    flask db upgrade
    ./bin/load_fixtures # seed the DB with sample DX codes
fi

exec flask run --host=0.0.0.0 --port=$PORT
