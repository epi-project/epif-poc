FROM ubuntu:20.04

RUN apt-get update && apt-get install --no-install-recommends -y \
	python3 \
	python3-pip \ 
	asyncio \
	websockets 

ADD client.py client.py

ENTRYPOINT ["./client.py"]

