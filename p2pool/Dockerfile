#######################################################################
# Dockerfile to add a p2pool mining server to a base Ubuntu server
#
# Based on saracen9/supervisor
#######################################################################

FROM saracen9/supervisor
MAINTAINER James Veitch <james@jamesveitch.com>
ENV DEBIAN_FRONTEND noninteractive

## BUILD
# install pre-reqs
RUN apt-get update
RUN apt-get install -y build-essential \
    libtool \
    autotools-dev \
    autoconf \
    pkg-config \
    libssl-dev \
    libboost-all-dev \
    libminiupnpc-dev \
    bsdmainutils


# BITCOIN
# install bitcoin (keep it simple)
RUN apt-get install -y software-properties-common &&\
    apt-add-repository -y ppa:bitcoin/bitcoin &&\
    apt-get update &&\
    apt-get install -y bitcoind

# add supervisor configuration into default folder
ADD configs/bitcoind.sv.conf /etc/supervisor/conf.d/

# LITECOIN
# install litecoin

#RUN git clone https://github.com/litecoin-project/litecoin.git &&\
#    cd litecoin &&\
#    LITECOIN_ROOT=$(pwd) &&\
#    BDB_PREFIX="${LITECOIN_ROOT}/db4" &&\
#    mkdir -p $BDB_PREFIX

#RUN wget 'http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz'
#RUN tar -xzvf db-4.8.30.NC.tar.gz &&\
#    cd db-4.8.30.NC/build_unix/ &&\
#    ../dist/configure --enable-cxx --disable-shared --with-pic --prefix=$BDB_PREFIX &&\
#    make install

#RUN cd litecoin &&\
#    ./autogen.sh &&\
#    ./configure --enable-upnp-default LDFLAGS="-L${BDB_PREFIX}/lib/" CPPFLAGS="-I${BDB_PREFIX}/include/" &&\
#    make &&\
#    strip src/litecoind &&\
#    make install

# add supervisor configuration into default folder
#ADD configs/bitcoind.sv.conf /etc/supervisor/conf.d/

# P2Pool
# install p2pool
RUN apt-get install -y python-zope.interface \
    python-twisted \
    python-twisted-web \
    libncurses-dev \
    libffi-dev
RUN git clone --recursive https://github.com/forrestv/p2pool.git &&\
    cd p2pool/litecoin_scrypt &&\
    python setup.py install &&\
    cd .. &&\
    ./configure &&\
    make

RUN cd p2pool &&\
    tar -cvzf web-static.backup.tar.gz web-static/ &&\
    rm web-static/* &&\
    git clone https://github.com/hardcpp/P2PoolExtendedFrontEnd.git &&\
    mv P2PoolExtendedFrontEnd/* web-static/



## Configs
ADD scripts /opt/scripts
RUN python /opt/scripts

## PORTS
# 8333/tcp  # bitcoin peer to peer
# 10333/tcp # litecoin peer to peer
# 8334/tcp  # namecoin peer to peer
# 8337/tcp  # ixcoin peer to peer
# 6334/tcp  # devcoin peer to peer
# 7337/tcp  # i0coin peer to peer
# 8492/tcp  # fusioncoin peer to peer
# 9333/tcp  # P2pool peer to peer
# 9332/tcp  # P2Pool connections and Web interface
# 9327/tcp  # P2Pool miner connections
EXPOSE 8333 8337 6334 73337 8492 9333 10333 9327

## STARTUP
# default initialisation command
