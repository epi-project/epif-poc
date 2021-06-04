FROM ubuntu:20.04

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 \
    python3-pip \
    iptables \
 && rm -rf /var/lib/apt/lists/*

ADD rules.sh rules.sh
ENTRYPOINT [ "./rules.sh"]


