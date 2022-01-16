FROM python:3.9.5-slim

RUN mkdir -p /opt
COPY . /opt/
WORKDIR /opt

RUN apt update
RUN apt install -y libpq-dev build-essential
RUN pip install pipenv
RUN pipenv install

ENTRYPOINT []
CMD pipenv run uvicorn main:app --host 0.0.0.0 --reload
