from keras_cv.models import StableDiffusion
from PIL import Image


def generate_image(prompt: str, name: str):
    model = StableDiffusion(img_height=450, img_width=900)
    img = model.text_to_image(
        prompt=prompt,
        batch_size=1,  # How many images to generate at once
        num_steps=25,  # Number of iterations (controls image quality)
        seed=123,  # Set this to always get the same image from the same prompt
    )
    image_path = f"./output/{name}.jpg"
    Image.fromarray(img[0]).save(image_path)


if __name__ == "__main__":
    generate_image(
        "Generate an image of a person using the NVIDIA Canvas application to draw a realistic mountain, river, and clouds. The image should showcase the impressive elements generated by the application based on the user's input.",
        "test",
    )
