from keras_cv.models import StableDiffusion
from PIL import Image

def generate_image(prompt: str):
    model = StableDiffusion(img_height=512, img_width=512)
    img = model.text_to_image(
        prompt=prompt,
        batch_size=1,  # How many images to generate at once
        num_steps=25,  # Number of iterations (controls image quality)
        seed=123,  # Set this to always get the same image from the same prompt
    )
    Image.fromarray(img[0]).save("./data/image.png")