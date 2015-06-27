#######################################################################
# Dockerfile to add a Tor service to a base Ubuntu server
#
# Based on saracen9/supervisor
#######################################################################

FROM saracen9/supervisor
MAINTAINER James Veitch <james@jamesveitch.com>
ENV DEBIAN_FRONTEND noninteractive

# BUILD

# install tor
ADD tor.list /etc/apt/sources.list.d/
RUN gpg --keyserver keys.gnupg.net --recv 886DDD89 &&\
    gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -
RUN apt-get update
RUN apt-get install -y tor deb.torproject.org-keyring

# add supervisor configuration into default folder
ADD tor.sv.conf /etc/supervisor/conf.d/

# add torrc configuration
ADD torrc /etc/tor/

# modify the system DNS resolver
RUN echo "nameserver 127.0.0.1" > /etc/resolv.conf

# install ufw
RUN apt-get install -y ufw
#RUN ufw enable &&\
#    ufw default deny incoming &&\
#    ufw default allow outgoing

# copy across iptables script and run
RUN mkdir -p /opt/scripts
ADD scripts/iptables.sh /opt/scripts/
RUN chmod +x /opt/scripts/*

# PORTS
EXPOSE 9050 53

# STARTUP
# default initialisation command
