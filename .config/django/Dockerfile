FROM python:3.11-alpine3.18

WORKDIR /app

RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --deploy

COPY .config/django/start.sh /
CMD [ "sh", "/start.sh" ]
