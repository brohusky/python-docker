FROM jrottenberg/ffmpeg:4.1-ubuntu

MAINTAINER Max Haze<eng.mahan.hazrati@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y build-essential git wget curl

WORKDIR /usr/src
# intall python essentials
RUN apt-get install -y zlib1g-dev libffi-dev libv4l-0
RUN apt-get install -y libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev libtk8.5 libgdm-dev libdb4o-cil-dev libpcap-dev
RUN apt-get install -y libsm6 libxext6

RUN wget -c https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz  -O - | tar -xz
RUN cd Python-3.7.2 && ./configure --enable-optimizations && make install
RUN apt-get upgrade -y python3

WORKDIR /

ENTRYPOINT []
