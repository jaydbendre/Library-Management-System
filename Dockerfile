FROM python:3

RUN mkdir /lms

WORKDIR /lms

COPY requirements.txt /lms/

RUN pip install -r requirements.txt

COPY . /lms/
