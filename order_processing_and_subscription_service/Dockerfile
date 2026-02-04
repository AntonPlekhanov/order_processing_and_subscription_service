FROM python:3.9-alpine3.16


COPY requirements.txt /temp/requirements.txt
COPY service /service
WORKDIR /service
EXPOSE 8000


RUN apk add --no-cache postgresql-client build-base postgresql-dev python3-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-adduser

USER service-adduser






