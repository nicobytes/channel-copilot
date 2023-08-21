from keras_cv.models import StableDiffusion
from PIL import Image

def generate_image(prompt: str, name: str):
    model = StableDiffusion(img_height=900, img_width=450)
    img = model.text_to_image(
        prompt=prompt,
        batch_size=1,  # How many images to generate at once
        num_steps=25,  # Number of iterations (controls image quality)
        seed=123,  # Set this to always get the same image from the same prompt
    )
    image_path = f"./output/{name}.jpg"
    Image.fromarray(img[0]).save(image_path)


if __name__ == "__main__":
    generate_image('A beautiful image of a sunset over the ocean.', 'test')