FROM python:3.10-slim
MAINTAINER Tim Schopinski

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
COPY ./requirements.dev.txt /requirements.dev.txt
COPY ./scripts /scripts
ARG DEV=false

RUN pip3 install -r requirements.txt
RUN if [ $DEV = "true" ]; \
    then pip3 install -r requirements.dev.txt ; \
    fi
RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web && chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER user
CMD ["run.sh"]