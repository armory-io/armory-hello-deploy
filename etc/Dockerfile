FROM ruby

RUN gem install --no-ri --no-rdoc fpm
RUN fpm --version

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-all \
    python-all


# upgrade pip
RUN easy_install3 -U pip


RUN pip3 install \
  nose==1.3.7 \
  stdeb==0.8.5 \
  datadog==0.16.0

ADD ./armory/ /home/armory/armory
ADD ./setup.py  /home/armory/setup.py
ADD ./etc/armory-hello-deploy.conf  /home/armory/etc/armory-hello-deploy.conf
ADD ./etc/server-env /etc/default/server-env

WORKDIR /home/armory/

RUN pip3 install -e .
