

import asyncio
import websockets
import serverhandle

async def response(websocket, path):
        print("waiting for a request")
        message = await websocket.recv()
#       message = message.encode('utf-8')
        print(f"We got the message from the client: {message}")
#       await websocket.send("Welcome to the Encryption server!")
        reply = serverhandle.BF(message)
        print(f"The decrypted format {reply}")
        await websocket.send(reply)

start_server = websockets.serve(response, '<Encprypt IP>', port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

