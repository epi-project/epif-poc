FROM ubuntu:20.04

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 \
    python3-pip \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install \
    starlette \
    uvicorn

ADD server.py server.py

EXPOSE 8000
ENTRYPOINT [ "uvicorn", "server:app", "--host", "0.0.0.0" ]
