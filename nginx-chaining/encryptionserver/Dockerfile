FROM ubuntu:18.04
WORKDIR /usr/src/app
VOLUME /usr/src/app
RUN apt-get update && apt-get -y upgrade && apt-get install -y \
#    sudo \
#    python3.7 \
    python3.7 \
    python3-pip
RUN ln -sf /usr/bin/python3.7 /usr/bin/python3
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install asyncio \
#    sys \
    websocket-client2 \
    websockets \
#    websocket \
    Crypto \
#    base64 \
    AES \
    pycryptodome \
    crypto-utils

RUN apt-get install bash
#sudo ln -s /usr/bin/python3 /usr/bin/python
ADD relay.py relay.py
ADD handleServer.py handleServer.py
#ADD entrypoint.sh entrypoint.sh
#RUN chmod +x entrypoint.sh
#ARG SERVER_IP
#RUN python3 relay.py ${SERVER_IP}
#ENV SERVER_IP $SERVER_IP
ENTRYPOINT ["python3", "relay.py"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]

