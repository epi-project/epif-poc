FROM ubuntu:20.04

RUN apt-get update -y && apt-get install iptables sudo -y \
    python3 \
    python3-pip \
    iptables \
    net-tools \
    iputils-ping \
 && rm -rf /var/lib/apt/lists/*
ADD rules.sh rules.sh
RUN chmod +x rules.sh
CMD [ "./rules.sh"]
#EXPOSE 1234:1234/tcp
ENTRYPOINT ["tail", "-f", "/dev/null"]

