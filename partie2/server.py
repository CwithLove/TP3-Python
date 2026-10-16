
import json
import math
from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import FileResponse, JSONResponse


app = FastAPI()

BASE_DIR = Path(__file__).parent
connected_clients = []

SHAPES = {
    "point": ["x", "y"],
    "line": ["x1", "y1", "x2", "y2"],
    "circle": ["x", "y", "radius"],
    "rectangle": ["x", "y", "width", "height"],
    "square": ["x", "y", "cote"]
}


# Validate the received shape
def validate_shape(data):
    if not isinstance(data, dict):
        return "JSON body must be an object"

    shape = data.get("shape")

    if shape not in SHAPES:
        return "Unknown shape"

    for field in SHAPES[shape]:
        if field not in data:
            return f"Missing parameter: {field}"

        value = data[field]

        if type(value) not in (int, float) or not math.isfinite(value):
            return f"Invalid number: {field}"

        if field in ("radius", "width", "height", "cote"):
            if value <= 0:
                return f"{field} must be positive"

    color = data.get("color")

    if not isinstance(color, list) or len(color) != 3:
        return "Color must contain 3 RGB values"

    for value in color:
        if type(value) is not int or not 0 <= value <= 255:
            return "RGB values must be integers between 0 and 255"

    return None


# Serve the HTML drawing board
@app.get("/")
async def index():
    return FileResponse(BASE_DIR / "index.html")


# Receive drawing commands through HTTP
@app.post("/draw")
async def draw(request: Request):
    try:
        data = await request.json()
    except ValueError:
        return JSONResponse(
            {"error": "Invalid JSON"},
            status_code=400
        )

    error = validate_shape(data)

    if error:
        return JSONResponse(
            {"error": error},
            status_code=400
        )

    print("Shape received:", data)

    message = json.dumps(data)

    for client in connected_clients.copy():
        try:
            await client.send_text(message)
        except (WebSocketDisconnect, RuntimeError, OSError):
            if client in connected_clients:
                connected_clients.remove(client)

    return {
        "status": "success",
        "shape": data
    }


# Broadcast shapes to connected boards
@app.websocket("/ws")
async def websocket_handler(websocket: WebSocket):
    await websocket.accept()

    connected_clients.append(websocket)
    print("New board connected")

    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        print("Board disconnected")

    finally:
        if websocket in connected_clients:
            connected_clients.remove(websocket)


# Start the server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
