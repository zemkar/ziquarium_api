FROM python:3.10-alpine3.16


EXPOSE 8000

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1

COPY requirements.txt /usr/src/app

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . /usr/src/app

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]