FROM python:3.7.3-slim-stretch

WORKDIR /home/punsy
ADD requirements.txt .

RUN apt-get update && \
    apt-get upgrade -y --no-install-recommends && \
    apt-get install -y --no-install-recommends curl && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN curl -O http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b

ADD . .
RUN ./ops/normalise.py cmudict-0.7b

