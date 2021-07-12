FROM ubuntu:20.04

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 \
    python3-pip
RUN pip3 install asyncio \
    websockets \
    websocket \
    websocket-client \
    Crypto \
    AES \
    pycryptodome

RUN apt-get install bash

ADD client.py client.py

ENTRYPOINT ["python3", "client.py"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]


