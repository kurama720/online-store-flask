FROM python:3.9-slim as builder

ENV PYTHONUNBUFFERED 1

WORKDIR /backend

RUN set -xe \
 && apt-get update -q \
 && apt-get autoremove -y \
 && apt-get clean -y \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /backend/wheels -r requirements.txt

FROM python:3.9-slim

EXPOSE 8000

#COPY ./requirements.txt ./
#
#RUN pip install -r requirements.txt

WORKDIR /backend

COPY --from=builder /backend/wheels /wheels

COPY --from=builder /backend/requirements.txt .

RUN pip install --no-cache /wheels/*


CMD ["flask", "run"]