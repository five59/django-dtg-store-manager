FROM python:3.5
ENV PYTHONUNBUFFERED 1

USER root
RUN mkdir /code

WORKDIR /code

RUN apt-get update && apt-get upgrade -y && apt-get install graphviz -y

ADD ./code /code/

RUN mkdir -p /root/.ptpython && touch /root/.ptpython/config.py
RUN pip install -r requirements.txt
