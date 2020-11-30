FROM ubuntu:20.04

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 \
    python3-pip \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install \
    httpx

ADD client.py client.py

ENTRYPOINT [ "./client.py" ]
