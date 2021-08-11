# pull official base image
FROM python:3
COPY . /usr/src/app
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV  PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip3 install -r requirements.txt