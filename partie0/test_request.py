import requests
import webbrowser
import subprocess


def count_num_breeds():
    url = "https://dog.ceo/api/breeds/list/all"

    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        data = response.json()
        breeds = data["message"]
        return len(breeds)
    else:
        print("Erreur HTTP :", response.status_code)
        return None
    
def display_random_dog():
    url = "https://dog.ceo/api/breeds/image/random"

    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        data = response.json()
        image_url = data["message"]
        subprocess.run(["cmd.exe", "/c", "start", "", image_url])
        # webbrowser.open(image_url) Operation not supported in this environment
    else:
        print("Erreur HTTP :", response.status_code)


# print(count_num_breeds())
print(display_random_dog())