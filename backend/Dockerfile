# pythonのバージョンは任意
FROM python:3.12.2

WORKDIR /usr/src/app

COPY ./ /usr/src/app/
COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install flask-restful