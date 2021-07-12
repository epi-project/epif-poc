from websocket import create_connection
from Crypto.Cipher import AES
from Crypto.Util import Counter

IV = b'1234567891234567'
iv_int = int.from_bytes(IV, byteorder='big')
new_counter = Counter.new(128, initial_value=iv_int)

key = "H"*32
key = bytes(key, 'utf-8')

# Encrypt data
def encrypt(msg):
#        msg = bytes(msg, 'utf-8')
        encrypto = AES.new(key, AES.MODE_CTR, counter= new_counter)
        return encrypto.encrypt(msg)
# Decrypt data
def decrypt(msg):
#        msg = bytes(msg, 'utf-8')
        decrypto = AES.new(key, AES.MODE_CTR, counter= new_counter)
        return decrypto.decrypt(msg)

def BF(msg):
        socket = create_connection("ws://172.16.238.13:5000")  #, subprotocols=["binary", "base64"])
        print("Connection with the server is established. Now ecrypting...")
        socket.send(encrypt(msg))
        decryptmsg = decrypt(socket.recv())
        return decryptmsg

