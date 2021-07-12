FROM ubuntu:20.04

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 \
    python3-pip
RUN pip3 install asyncio \
    websockets \
#    websocket \
    websocket-client2 \
    Crypto \
    AES \
#    base64 \
    pycryptodome \
    crypto-utils

RUN apt-get install bash

ADD server.py server.py

ENTRYPOINT ["python3", "server.py"]
