import sys
import asyncio
import websockets
import time

async def message():
        async with websockets.connect("ws://172.16.238.10:8080") as socket: #, subprotocols=["binary", "base64"]) as socket: #This a connection to the NGINX
                #msg = print("What do you want to send: ")
                #for msg in sys.argv:
                #msg = sys.argv[0]
#                for i in range(5):
                 msg = b'hello'
                 await socket.send(msg)
                 start = time.time()
                 print(await socket.recv())
                 end = time.time()
                 print(end - start)
asyncio.get_event_loop().run_until_complete(message())


