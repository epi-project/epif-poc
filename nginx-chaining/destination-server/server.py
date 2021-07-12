import asyncio
import websockets
from Crypto.Cipher import AES
from Crypto.Util import Counter

IV = b'1234567891234567'
iv_int = int.from_bytes(IV, byteorder='big')
new_counter = Counter.new(128, initial_value=iv_int)

key = "H"*32
key = bytes(key, 'utf-8')

# Encrypt data
def encrypt(msg):
        encrypto = AES.new(key, AES.MODE_CTR, counter= new_counter)
        return encrypto.encrypt(msg)
# Decrypt data
def decrypt(msg):
        msg = bytes(msg, 'utf-8')
        decrypto = AES.new(key, AES.MODE_CTR, counter= new_counter)
        return decrypto.decrypt(msg)

async def response(websocket, path):
        message = await websocket.recv()
##        message = bytes(message, 'utf-8')
#        message = decrypt(message)
        print(f"We got the message from the client: {message}")
        msg = "I can confirm I got your message!"
#        msg = bytes(msg, 'utf-8')
#        await websocket.send(encrypt(msg))
        await websocket.send(msg)

start_server = websockets.serve(response, '172.16.238.13', 5000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

