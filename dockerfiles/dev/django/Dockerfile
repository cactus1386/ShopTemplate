FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /user/src/app

COPY ./requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./core .
