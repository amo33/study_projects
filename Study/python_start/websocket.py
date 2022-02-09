# Server
import asyncio          
import websockets          

async def accept(websocket, path):
    while True:
        data = await websocket.recv()
        print("receive : " + data)
        await websocket.send("ws_srv send data = " + data)

start_server = websockets.serve(accept, "0.0.0.0", 0000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
