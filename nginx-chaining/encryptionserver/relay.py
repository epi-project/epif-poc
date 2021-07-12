
import asyncio
import sys
import websockets
import handleServer

async def response(websocket, path):
        print("waiting for a request")
        message = await websocket.recv()
#       message = message.encode('utf-8')
        print(f"We got the message from the client: {message}")
#        message = str(message)
#        await websocket.send("Welcome to the Encryption server!")
        reply = handleServer.BF(message) #, sys.argv)
#        print(f"The decrypted format {reply}")
        await websocket.send(reply)

start_server = websockets.serve(response, '172.16.238.12', 1235)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

