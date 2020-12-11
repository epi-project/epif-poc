#Make two bridge networks for different containarised nodes running
sudo docker network create --driver bridge --subnet 192.168.100.0/24 --ip-range 192.168.100.0/24 my-bridge-network1
sudo docker network create --driver bridge --subnet 192.168.101.0/24 --ip-range 192.168.101.0/24 my-bridge-network2
#Build node-a 
sudo docker build -t epi-poc-demo/node-a node-a 
#Run node-a
sudo docker run -it --network my-bridge-network1 epi-poc-demo/node-a
#Build b
sudo docker build -t epi-poc-demo/node-b node-b
#Run b
sudo docker run -it --network my-bridge-network2 epi-poc-demo/node-b
#Build firewall
sudo docker build -t epi-poc-demo/firewall firewall
#Run firewall 
sudo docker run -it --network my-bridge-network epi-poc-demo/firewall 
#Flush
iptables -F
#Enable communication with firewall
iptables -I DOCKER-USER -s 192.168.101.2 <node-b IP> -d 192.168.100.3 <Firewall IP>  -j ACCEPT
iptables -I DOCKER-USER -d 192.168.101.2 -s 192.168.100.3 -j ACCEPT
#redirecting rule 
sudo iptables -t nat -A PREROUTING -s 192.168.101.2 -j DNAT -p tcp -d 192.168.100.3 --to-destination 192.168.100.2
iptables -t nat -A POSTROUTING -j MASQUERADE
