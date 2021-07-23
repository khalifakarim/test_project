FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

WORKDIR /usr/src/app/

COPY Pipfile* /usr/src/app/

RUN pip install pipenv && pipenv install --deploy --system

COPY . /usr/src/app/

CMD ./entrypoint.sh