FROM python:3.10

USER root:root

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -qqy git build-essential unixodbc-dev ssh wget &&\
    apt-get clean

RUN groupadd -g 1000 app && \
    useradd -g 1000 -u 1000 --system --create-home app

RUN pip install poetry \
    && poetry config virtualenvs.in-project true

USER app

RUN poetry config virtualenvs.in-project true

WORKDIR /code
