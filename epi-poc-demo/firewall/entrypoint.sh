#!/bin/bash

#Enable IP Forwarding for NAT
#echo "1" > /proc/sys/net/ipv4/ip_forward

#Forward incoming packets on 192.168.0.3 at wlan0 interface to 127.0.0.1
iptables -t nat -A PREROUTING -p tcp -i eth0 -d 192.168.100.3 -j DNAT --to 192.168.100.2
#iptables -t nat -A OUTPUT ! -d /32 -o eth0 -p tcp -m tcp -j REDIRECT --to-ports 42000
