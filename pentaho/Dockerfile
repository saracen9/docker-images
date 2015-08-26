#######################################################################
# Dockerfile to build a base ubuntu server image with
# Supervisor (http://supervisord.org/) as a scheduler and
# process controller.
#
# Based on Ubuntu and borrowed from the excellent
# https://github.com/Krijger/docker-cookbooks/tree/master/supervisor
#######################################################################

FROM saracen9/supervisor
MAINTAINER James Veitch <james@jamesveitch.com>
ENV DEBIAN_FRONTEND noninteractive

# BUILD
# update the system
RUN apt-get update && apt-get upgrade -y

# install pre-reqs
RUN apt-get install -y openjdk-7-jre libwebkitgtk-1.0.0 unzip

# grab latest pentaho binaries
RUN mkdir -p /opt/pentaho && cd /opt/pentaho

RUN echo -e "\nDownloading: Business Analytics Platform"
RUN wget http://sourceforge.net/projects/pentaho/files/Business%20Intelligence%20Server/5.4/biserver-ce-5.4.0.1-130.zip

RUN echo -e "\nDownloading: Data Integration (kettle)"
RUN wget http://sourceforge.net/projects/pentaho/files/Data%20Integration/5.4/pdi-ce-5.4.0.1-130.zip

RUN echo -e "\nDownloading: Report Designer (reporting)"
RUN wget http://sourceforge.net/projects/pentaho/files/Report%20Designer/5.4/prd-ce-5.4.0.1-130.zip

RUN echo -e "\nDownloading: Mondrian"
RUN wget http://downloads.sourceforge.net/project/mondrian/mondrian/mondrian-3.10.0/mondrian-3.10.0.1-130.jar

RUN echo -e "\nDownloading: Aggregation Designer"
RUN wget http://sourceforge.net/projects/mondrian/files/aggregation%20designer/5.4/pad-ce-5.4.0.1-130.zip

RUN echo -e "\nDownloading: Schema Workbench"
RUN wget http://sourceforge.net/projects/mondrian/files/schema%20workbench/3.10.0/psw-ce-3.10.0.1-130.zip

RUN echo -e "\nDownloading: Metadata Editor"
RUN wget http://sourceforge.net/projects/pentaho/files/Pentaho%20Metadata/5.4/pme-ce-5.4.0.1-130.zip

RUN echo -e "\nDownloading: Weka (data mining)"

RUN echo -e "\nDone. Downloads complete."

RUN for f in *.zip; do unzip "$f"; done;

# supervisor base configuration
ADD configs/pentaho.conf /etc/supervisor/conf.d/pentaho.conf

# PORTS
EXPOSE 8080 8009

# STARTUP
# default initialisation command
CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf"]
