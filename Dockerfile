FROM python:3.7-alpine
MAINTAINER Yao Adzaku <yao.adzaku@gmail.com>

# install dependencies
RUN apk update && \
    apk add --no-cache gcc python-dev bash musl-dev \
    postgresql-dev \
    libffi-dev \
    postgresql-client

EXPOSE 5000

COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install --system --deploy

ENTRYPOINT ["bash", "/app/entrypoint.sh"]
