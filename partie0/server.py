import asyncio
from websockets.asyncio.server import serve

async def handler(websocket):
    message = await websocket.recv()

    print("Message reçu :", message)

    count = message.count("b")

    await websocket.send(f'{count} caractère(s) "b"')
    
async def main():
    async with serve(handler, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever
        
asyncio.run(main())