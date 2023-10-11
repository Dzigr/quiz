FROM python:3.11

RUN mkdir /quiz_app

WORKDIR /quiz_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
