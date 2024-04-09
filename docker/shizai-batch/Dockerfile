# FROM python:3.12-bullseye
# FROM python:3.6.15-bullseye
FROM python:3.10.13-bullseye

COPY batch /var/service/batch
COPY common /var/service/common

RUN mkdir -p /var/service/run

EXPOSE 7000

COPY requirements.txt /var/tmp
RUN pip install -r /var/tmp/requirements.txt
