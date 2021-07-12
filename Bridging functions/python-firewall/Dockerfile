FROM ubuntu:20.04

RUN apt-get update -y && apt-get install iptables sudo -y \
    python3 \
    python3-pip \
    iptables \
    net-tools \
    iputils-ping \
    install --upgrade python-iptables \
 && rm -rf /var/lib/apt/lists/*
ADD rules.py rules.py
RUN chmod +x rules.py
#CMD [ "./rules.sh"]
#EXPOSE 1234:1234/tcp
ENTRYPOINT ["tail", "-f", "/dev/null"]
#EXPOSE 1234:1234/tcp
#ENTRYPOINT["rules.sh"]

