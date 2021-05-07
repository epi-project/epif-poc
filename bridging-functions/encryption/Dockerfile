FROM ubuntu:20.04

WORKDIR /encryption

RUN apt-get update && apt-get install --no-install-recommends -y \
    sudo \
    curl \
    iptables \
    nano \
    python3 \
    python3-pip \
    net-tools \
    iputils-ping \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install \

ADD encrypt-server.py encrypt-server.py
ADD entrypoint.sh entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]
