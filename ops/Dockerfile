FROM python:3.8-slim-buster

WORKDIR /home/punsy
ADD requirements.txt .

RUN apt-get update && \
    apt-get upgrade -y --no-install-recommends && \
    apt-get install -y --no-install-recommends curl && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ADD ops/normalise.py .
RUN mkdir -p punsy/data && \
    curl -O http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b && \
    ./normalise.py cmudict-0.7b punsy/data/cmudict-0.7b.utf8
