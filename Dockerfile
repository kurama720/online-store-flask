FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 3000

RUN set -xe \
 && apt-get update -q \
 && apt-get install -y --no-install-recommends gettext poppler-utils\
 && apt-get autoremove -y \
 && apt-get clean -y \
 && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install -r requirements.txt

WORKDIR /

CMD flask run