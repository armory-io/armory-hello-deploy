FROM ubuntu:trusty

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-all \
    python-all \
    debhelper

ADD ./armory/ /home/armory/armory
ADD ./setup.py  /home/armory/setup.py
ADD ./etc/server-env /etc/default/server-env

WORKDIR /home/armory/

RUN pip3 install \
  nose==1.3.7 \
  stdeb==0.8.5

RUN pip3 install -e .

CMD armory/start_server.py
