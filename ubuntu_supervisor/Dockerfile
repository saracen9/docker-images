#######################################################################
# Dockerfile to build a base ubuntu server image with
# Supervisor (http://supervisord.org/) as a scheduler and
# process controller.
#
# Based on Ubuntu and borrowed from the excellent
# https://github.com/Krijger/docker-cookbooks/tree/master/supervisor
#######################################################################

FROM ubuntu:14.04
MAINTAINER James Veitch <james@jamesveitch.com>
ENV DEBIAN_FRONTEND noninteractive

# BUILD
# update the system
RUN apt-get update && apt-get upgrade -y

# install useful tools
RUN apt-get install -y \
    nano \
    git \
    p7zip-full \
    wget \
    curl

# supervisor installation &&
# create directory for child images to store configuration in
RUN apt-get -y install supervisor && \
    mkdir -p /var/log/supervisor && \
    mkdir -p /etc/supervisor/conf.d

# supervisor base configuration
ADD configs/supervisor.conf /etc/supervisor/supervisor.conf

# STARTUP
# default initialisation command
CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf"]
