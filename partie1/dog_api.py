
import requests


def get_breeds():
    url = "https://dog.ceo/api/breeds/list/all"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        return list(data["message"].keys())

    except (requests.RequestException, ValueError, KeyError, TypeError) as error:
        print("Error fetching dog breeds:", error)
        return []


def get_dog_image(breed):
    url = f"https://dog.ceo/api/breed/{breed}/images/random"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        return data["message"]

    except (requests.RequestException, ValueError, KeyError, TypeError) as error:
        print("Error fetching dog image:", error)
        return None
