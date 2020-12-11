#FROM python:3.10.0a2-buster
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

#ADD entrypoint.sh entrypoint.sh

#RUN ["chmod", "+x", "entrypoint.sh"]

#COPY fw-server.py fw-server.py

#ENTRYPOINT [ "./entrypoint.sh" ]

#CMD ["python", "fw-server.py"]
