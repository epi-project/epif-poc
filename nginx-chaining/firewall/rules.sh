#! /bin/bash
sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
iptables -A FORWARD -i eth1 -j ACCEPT
iptables -A FORWARD -o eth1 -j ACCEPT
iptables -I INPUT -p tcp -m tcp --dport 1234 -j ACCEPT
#iptables -A INPUT -m state --state NEW -i ! -j ACCEPT

iptables -t nat -A PREROUTING -p tcp --dport 1234 -j DNAT --to-destination 172.16.238.10:8081
##iptables -A FORWARD -i eth0 -p tcp --dport 80 -d 172.31.0.23 -j ACCEPT
iptables -t nat -A POSTROUTING -p tcp --dport 1234 -j MASQUERADE
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
iptables --append FORWARD --in-interface eth1 -j ACCEPT
##iptables -t nat -A PREROUTING -p tcp --dport 1234 -m conntrack  --ctstate NEW -j DNAT  --to 192.168.33.20:8081
##iptables -t nat -A PREROUTING -m conntrack  --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A POSTROUTING -t nat -j MASQUERADE
iptables-save


