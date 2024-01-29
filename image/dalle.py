import openai
import requests


def generate_image(prompt: str, name: str):
    response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
    url = response["data"][0]["url"]
    response = requests.get(url, stream=True)
    response.raise_for_status()
    image_path = f"./output/{name}.jpg"
    with open(image_path, "wb") as archivo:
        for chunk in response.iter_content(chunk_size=8192):
            archivo.write(chunk)
    return url
