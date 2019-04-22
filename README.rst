===============================
mpharma
===============================

mPharma diagnosis API


Quickstart
----------

The [fixtures](./fixtures) are a subset of the in https://github.com/kamillamagna/ICD-10-CSV.

Run the following commands to bootstrap your environment ::

    git clone https://github.com/rpip/mpharma
    cd mpharma
    pipenv shell --three #use Python 3 if you have that installed locally, or omit the `three` to use Python 2
    pipenv install --dev
    cp .env.example .env

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration ::

    flask db init
    flask db migrate
    flask db upgrade
    ./bin/load_fixtures # seed the DB with sample DX codes.
    flask run       # start the flask server


This will output the following:

     * Serving Flask app "autoapp.py" (lazy loading)
     * Environment: development
     * Debug mode: on
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 474-453-555

Routes
--------

- Diagnosis Code collection endpoint `http://127.0.0.1:5000/diagnosis`
- Diagnosis Code endpoint `http://127.0.0.1:5000/diagnosis/:id`



Docker
----------

    docker-compose up


Shell
-----

To open the interactive shell, run ::

    flask shell

By default, you will have access to the flask ``app``.


Running Tests
-------------

To run all tests, run ::

    flask test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands ::

    flask db migrate

This will generate a new migration script. Then run ::

    flask db upgrade

To apply the migration.

For a full migration command reference, run ``flask db --help``.
