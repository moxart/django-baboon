FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /home/app
RUN addgroup -S app && adduser -S app -G app

ENV HOME=/home/app
ENV HOME_APP=/home/app/web

RUN mkdir $HOME_APP
WORKDIR $HOME_APP

COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    && pip install -r requirements.txt \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

COPY . $HOME_APP

RUN chmod -x ./scripts/*
RUN chown -R app:app $HOME_APP
RUN chmod -R 755 $HOME_APP

USER app

ENTRYPOINT ["./scripts/entrypoint.sh"]