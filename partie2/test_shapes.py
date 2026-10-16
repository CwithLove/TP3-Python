
import requests


URL = "http://localhost:8080/draw"

shapes = [
    {
        "shape": "point",
        "x": 100,
        "y": 100,
        "color": [255, 0, 0]
    },
    {
        "shape": "line",
        "x1": 150,
        "y1": 100,
        "x2": 300,
        "y2": 200,
        "color": [0, 0, 255]
    },
    {
        "shape": "circle",
        "x": 400,
        "y": 250,
        "radius": 60,
        "color": [0, 180, 0]
    },
    {
        "shape": "rectangle",
        "x": 500,
        "y": 100,
        "width": 150,
        "height": 80,
        "color": [255, 165, 0]
    },
    {
        "shape": "square",
        "x": 200,
        "y": 300,
        "cote": 80,
        "color": [150, 0, 200]
    }
]


for shape in shapes:
    response = requests.post(URL, json=shape, timeout=5)

    print(
        shape["shape"],
        "-> HTTP",
        response.status_code
    )


# Test invalid data
invalid_shape = {
    "shape": "circle",
    "x": 100,
    "y": 100,
    "radius": -20,
    "color": [255, 0, 0]
}

response = requests.post(
    URL,
    json=invalid_shape,
    timeout=5
)

print("Invalid circle -> HTTP", response.status_code)
print("Error:", response.json())
