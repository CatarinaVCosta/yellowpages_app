FROM python:3.6

RUN mkdir /app
WORKDIR /app
ADD . /app

RUN pip install Pillow
RUN pip install Django
