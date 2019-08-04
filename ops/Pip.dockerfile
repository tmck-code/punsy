FROM python:3.7.3-slim-stretch

WORKDIR /home/punsy

RUN python -m pip install --upgrade pip setuptools wheel

ADD . .
