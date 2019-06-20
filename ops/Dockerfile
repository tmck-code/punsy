FROM python:3.7.3-slim-stretch

ADD requirements.txt .

RUN apt-get update \
    && apt-get upgrade -y --no-install-recommends
RUN
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

RUN apt-get install -y --no-install-recommends curl

WORKDIR /home/punsy
ADD . .
