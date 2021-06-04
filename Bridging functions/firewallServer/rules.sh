#!/bin/bash
sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'
iptables -t nat -A PREROUTING -p tcp --dport 1234 -j DNAT --to-destination <proxy IP:port>
iptables -t nat -A POSTROUTING -p tcp --dport 1234 -j MASQUERADE
iptables-save


