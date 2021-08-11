# pull official base image
FROM python:3.9-alpine

# set work directory
WORKDIR .

# set environment variables
ENV  PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src/app/requirements.txt

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev postgresql-dev python3-dev \
    && pip3 install --upgrade pip \
    && pip3 install psycopg2 \
    && pip3 install --upgrade pip setuptools wheel \
    && pip3 install -r /usr/src/app/requirements.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY . /usr/src/app
