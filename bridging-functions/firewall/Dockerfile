FROM ubuntu:20.04

WORKDIR /firewall

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

ENTRYPOINT [ "./firewall.sh" ]
