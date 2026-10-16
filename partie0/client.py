import asyncio
import sys
from websockets.asyncio.client import connect


async def main():
    async def main():
    if len(sys.argv) < 2:
        print("Usage : python client.py <message>")
        return

    message = sys.argv[1]

    async with connect("ws://localhost:8765") as websocket:
        await websocket.send(message)

        response = await websocket.recv()
        print(response)


asyncio.run(main())