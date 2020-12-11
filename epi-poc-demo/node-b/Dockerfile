#FROM python:3.10.0a2-buster
FROM ubuntu:20.04

WORKDIR /node-b

RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    iptables \
    nano \
    python3 \
    python3-pip \
    net-tools \
    iputils-ping \
 && rm -rf /var/lib/apt/lists/*

#COPY node-b.py node-b.py

#CMD ["python", "node-b.py" ]


