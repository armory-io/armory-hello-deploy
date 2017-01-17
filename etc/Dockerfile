FROM ubuntu:trusty

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-all \
    python-all \
    debhelper

ADD ./src/ /home/armory/armory
ADD ./etc/server-env /etc/default/server-env

WORKDIR /home/armory/

RUN pip3 install \
  nose==1.3.7 \
  Flask==0.12 \
  stdeb==0.8.5

CMD armory/start_server.py
