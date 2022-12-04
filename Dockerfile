FROM python:3.10

USER root:root

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -qqy git build-essential unixodbc-dev ssh wget &&\
    apt-get clean

RUN pip install poetry \
    && poetry config virtualenvs.in-project true

RUN poetry config virtualenvs.in-project true

WORKDIR /code
