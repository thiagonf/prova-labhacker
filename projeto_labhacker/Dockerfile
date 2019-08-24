FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update -y && apt-get install libpq-dev python3-dev -y
RUN pip install -r requirements.txt
COPY . /code/