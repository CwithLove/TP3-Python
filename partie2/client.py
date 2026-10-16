
import requests


SERVER_URL = "http://localhost:8080/draw"

SHAPES = {
    "point": ["x", "y"],
    "line": ["x1", "y1", "x2", "y2"],
    "circle": ["x", "y", "radius"],
    "rectangle": ["x", "y", "width", "height"],
    "square": ["x", "y", "cote"]
}


def ask_number(name):
    while True:
        try:
            return float(input(f"{name}: "))
        except ValueError:
            print("Please enter a valid number.")


def ask_color():
    while True:
        try:
            values = input("RGB color (e.g. 255,0,0): ")
            color = [int(value.strip()) for value in values.split(",")]

            if len(color) == 3 and all(0 <= c <= 255 for c in color):
                return color

            print("RGB must contain three values from 0 to 255.")

        except ValueError:
            print("Invalid RGB color.")


def create_shape():
    print("\nAvailable shapes:")
    for shape in SHAPES:
        print("-", shape)

    shape = input("\nChoose a shape: ").lower().strip()

    if shape not in SHAPES:
        print("Unknown shape.")
        return None

    data = {"shape": shape}

    for field in SHAPES[shape]:
        data[field] = ask_number(field)

    data["color"] = ask_color()

    return data


def send_shape(data):
    try:
        response = requests.post(
            SERVER_URL,
            json=data,
            timeout=5
        )

        if response.status_code == 200:
            print("Shape sent successfully!")
        else:
            print("Server error:", response.json())

    except requests.RequestException as error:
        print("Connection error:", error)


def main():
    print("=== INTERACTIVE DRAWING CLIENT ===")

    while True:
        data = create_shape()

        if data is not None:
            send_shape(data)

        again = input("\nDraw another shape? (y/n): ").lower().strip()

        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
