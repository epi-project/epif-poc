
FROM ubuntu:20.04

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 \
    python3-pip \
    asyncio \
    websockets \
    Crypto
 && rm -rf /var/lib/apt/lists/*

ADD relay.py relay.py
ADD handleServer.py handleServer.py

ENTRYPOINT [ "./relay.py"]

