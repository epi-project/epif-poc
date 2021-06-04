import asyncio
import websockets

async def message():
        async with websockets.connect("ws://<Proxy IP: port1>", subprotocols=["binary", "base64"]) as socket: #This a connection to the NGINX
                msg = input("What do you want to send: ")
                await socket.send(msg)
                print(await socket.recv())

asyncio.get_event_loop().run_until_complete(message())


