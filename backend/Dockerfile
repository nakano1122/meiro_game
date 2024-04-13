FROM python:3.12.2

WORKDIR /usr/src/app

COPY ./ /usr/src/app/
COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --upgrade flask
RUN pip install -r requirements.txt
RUN apt-get update && \
    apt-get install -y sqlite3 libsqlite3-dev && \
    rm -rf /var/lib/apt/lists/*
RUN pip install flask_sqlalchemy