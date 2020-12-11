import os
import socket
import threading

HEADER = 64
PORT = 5050
FW = socket.gethostbyname(socket.gethostname())
ADDR = (FW, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
NODEB = "192.168.101.2"
BPORT = 5053
ADDR2 = (NODEB, BPORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.connect(ADDR2)

def handle_client(conn, addr):
    print(f"[FIREWALL CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
            def send(msg):
		message = msg.encode(FORMAT)
		msg_length = len(message)
		send_length = str(msg_length).encode(FORMAT)
		send_length += b' ' * (HEADER - len(send_length))
		server.send(send_length)
		server.send(message)
    		 print(server.recv(2048).decode(FORMAT))
	    send(f"{msg}")
	    #os.system(iptables -t nat -A OUTPUT ! -d 192.168.101.2 -o eth0 -p tcp -m tcp -j REDIRECT --to-ports 8082)
	    #os.system(iptables -t nat -A PREROUTING -p tcp -i eth0 -d 192.168.100.3 -j DNAT --to 192.168.100.2)
            #os.system(iptables -t nat -A PREROUTING -p tcp -i eth0 -d 192.168.100.3 -j DNAT --to 192.168.101.2)
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] firewall is running on {FW}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()


