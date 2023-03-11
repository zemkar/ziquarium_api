FROM python:3.10-alpine3.16


EXPOSE 8000

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1
# Django secret key
ENV SECRET_KEY=@!!django-insecure-#aaiogqnj2*de@&m5od7=fx8yh+8zy@aow5_0$(8#3_2i1-y3q
# Stripe test keys
ENV STRIPE_PK_KEY=pk_test_51MecxZK7eRk186VKGGCEA0WjB48f3jI8e74geU7HEfKbMk4enptqEb9rd4UvzVZhJMUx7ZDPWZ0HRa0f3Paf1B8t00QPnTpws4
ENV STIPE_SK_KEY=sk_test_51MecxZK7eRk186VKkLOSXBkXLueBhWg9HLyU25TUIZKMRxdu8ISJSLC3YY7LffTa5NuddYyIMKPCUwIb6K86OPDo00jLxpB0Oc
ENV STRIPE_WEBHOOK_SECRET=whsec_5298b8213ffbd95dd6a27605f0cce8dbf2676e4e7ddadb637754aad297b19a21
# Data base connection data
ENV DB_NAME=ziquarium_db
ENV DB_USER=ziquarium
ENV DB_PASSWORD=ZoFT1yPNjVmcqd2d74LuVRNKmOh3CstR
ENV DB_HOST=dpg-cg65ochmbg5ab7j6v4ug-a.frankfurt-postgres.render.com
ENV DB_PORT=5432
# URLs of site and API
ENV SERVER_URL=http://127.0.0.1:8000
ENV SITE_URL=http://127.0.0.1:3000

COPY requirements.txt /usr/src/app

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . /usr/src/app

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

# test superuser is admin:951Qsc62Ax3z