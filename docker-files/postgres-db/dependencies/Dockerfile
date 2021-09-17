FROM ubuntu:16.04
MAINTAINER "ArthurWuTw <lion811004@gmail.com>"

ARG CONTAINER_USER
ARG HOST_USER_GID
ARG HOST_USER_UID
ARG TIMEZONE

WORKDIR /tmp

# Disable interactive configuration
ENV DEBIAN_FRONTEND=noninteractive

# Setup the host's timezone
RUN apt-get update && \
  ln -sf /usr/share/zoneinfo${TIMEZONE:?} /etc/localtime && \
  apt-get install -y tzdata

# Create user
COPY create-user utils.sh ./
RUN ./create-user && \
  rm create-user utils.sh

# Install host's certification
RUN apt-get update && \
  apt-get install -y ca-certificates && \
  update-ca-certificates

# Install apt dependencies
COPY install-apt-dependencies utils.sh ./
RUN ./install-apt-dependencies && \
    rm install-apt-dependencies utils.sh

# Install Python3 Python2
COPY install-python utils.sh ./
RUN ./install-python && \
  rm install-python utils.sh

# Install pip3 package dependencies
COPY requirements.txt ./
RUN pip3 install --upgrade pip && \
  pip3 install -r ./requirements.txt && \
  rm requirements.txt

# Install Python-Postgresql and Apt-Postgresql
COPY install-postgresql utils.sh ./
RUN ./install-postgresql && \
  rm install-postgresql utils.sh

COPY enter-container-shell \
    infinite-loop \
    /usr/local/bin/
RUN chmod +x /usr/local/bin/infinite-loop
RUN chmod +x /usr/local/bin/enter-container-shell