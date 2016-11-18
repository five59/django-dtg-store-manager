FROM python:3.5
ENV PYTHONUNBUFFERED 1

USER root
RUN mkdir /code

WORKDIR /code

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y graphviz locales

RUN sed -i -e "s/# en_US.*/en_US.UTF-8 UTF-8/" /etc/locale.gen
RUN dpkg-reconfigure --frontend=noninteractive locales
RUN update-locale LANG=en_US.UTF-8

ENV LC_ALL=en_US.UTF-8

ADD ./code /code/

RUN mkdir -p /root/.ptpython && touch /root/.ptpython/config.py
RUN pip install --upgrade pip && pip install -r requirements.txt
