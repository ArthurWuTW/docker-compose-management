FROM ubuntu:20.04
MAINTAINER "ArthurWuTw <lion811004@gmail.com>"

ARG CONTAINER_USER
ARG HOST_USER_GID
ARG HOST_USER_UID
ARG TIMEZONE
ARG ECLIPSE_INSTALLATION_FILE_DIR

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

# Install apt-getable dependencies
RUN apt-get update \
    && apt-get install -y \
        build-essential \
        cmake \
        python \
        git \
        curl \
        openssh-server \
        git-core \
        net-tools \
        vim \
        gcc \
        iputils-ping

# Install zulu openjdk
COPY install-java utils.sh ./
RUN ./install-java
RUN rm install-java utils.sh

ENV PATH="/home/${CONTAINER_USER}/lib/zulu8.56.0.21-ca-jdk8.0.302-linux_x64/bin:${PATH}"
ENV JAVA_HOME="/home/${CONTAINER_USER}/lib/zulu8.56.0.21-ca-jdk8.0.302-linux_x64"

# Install eclipse
RUN apt-get install -y libswt-gtk*
COPY install-eclipse utils.sh eclipse_tar_dir/eclipse-jee-2020-03-R-incubation-linux-gtk-x86_64.tar.gz ./
RUN ./install-eclipse
RUN rm install-eclipse utils.sh eclipse-jee-2020-03-R-incubation-linux-gtk-x86_64.tar.gz

# Install tomcat
COPY install-tomcat utils.sh ./
RUN ./install-tomcat
RUN rm install-tomcat utils.sh
# Port 7001 configuration
COPY tomcat_conf_dir/server.xml /home/${CONTAINER_USER}/tomcat/apache-tomcat-9.0.52/conf/

# Install DBeaver
COPY install-dbeaver utils.sh ./
RUN ./install-dbeaver
RUN rm install-dbeaver utils.sh

# Copy deploy-spring-boot-project-from-git-by-dir
COPY deploy-spring-boot-project-from-git-by-dir ./
RUN ./deploy-spring-boot-project-from-git-by-dir
RUN rm deploy-spring-boot-project-from-git-by-dir
RUN rm -r spring-boot-project

COPY enter-container-shell \
    infinite-loop \
    /usr/local/bin/
RUN chmod +x /usr/local/bin/infinite-loop
RUN chmod +x /usr/local/bin/enter-container-shell
