FROM ubuntu:18.04
LABEL maintainer="Pieter Buteneers<pieter.buteneers@gmail.com>"

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install npm nodejs python3-pip git python-dev

#RUN npm name=configurable-http-proxy global=yes
RUN npm install -g configurable-http-proxy

RUN pip3 install jupyterhub jupyter numpy scipy matplotlib sklearn pandas

COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

COPY release/1/ /home/cs/tutorial/

COPY create_users.py /tmp/create_users.py

RUN python /tmp/create_users.py 1000 password

COPY jupyterhub /etc/init.d/jupyterhub

RUN update-rc.d jupyterhub defaults

CMD ["jupyterhub", "-f", "/etc/jupyterhub/jupyterhub_config.py"]
