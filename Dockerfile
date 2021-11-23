FROM ubuntu:20.04
LABEL maintainer="Pieter Buteneers<pieter.buteneers@gmail.com>"

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install nodejs
# Separate command to avoid location question for nodejs
RUN apt-get -y install python3-pip python-dev npm 

#RUN npm name=configurable-http-proxy global=yes
RUN npm install -g configurable-http-proxy

RUN pip3 install jupyterhub jupyter numpy scipy matplotlib sklearn pandas

COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

COPY release/1/ /home/cs/tutorial/

COPY create_users.py /tmp/create_users.py

RUN python3 /tmp/create_users.py 200 password

COPY jupyterhub /etc/init.d/jupyterhub

RUN update-rc.d jupyterhub defaults

CMD ["jupyterhub", "-f", "/etc/jupyterhub/jupyterhub_config.py"]
