FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

RUN set -xe \
 && apt-get update -q \
 && apt-get autoremove -y \
 && apt-get clean -y \
 && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

WORKDIR /backend

EXPOSE 8000

CMD flask run