FROM python:3

#This is for the main application
RUN /usr/local/bin/pip install \
    nose==1.3.7 \
    Flask==0.12

ADD ./armory /home/armory/armory
ADD ./setup.py /home/armory/setup.py
ADD ./etc/server-env /etc/default/server-env

WORKDIR /home/armory/

RUN pip3 install -e .

CMD /usr/local/bin/start_server.py
