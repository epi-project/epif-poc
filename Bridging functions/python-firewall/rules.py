import iptc

chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
rule = iptc.Rule()
rule.in_interface = "bf-net"
rule.src = "172.16.238.10"
target = iptc.Target(rule, "ACCEPT")
rule.target = target
chain.insert_rule(rule)
