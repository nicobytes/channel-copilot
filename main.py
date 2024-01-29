import settings
import typer
from transcript.audio import get_audio
from transcript.whisper import get_transcribe
from chains.summary_chain import summary_chain
from chains.youtube_chain import youtube_chain
from chains.thread_chain import thread_chain
from chains.dalle_chain import dalle_chain
from image.dalle import generate_image
from rich import print


app = typer.Typer()
output_dir = "./data/2024-01-25-migration"


@app.command()
def audio():
    video_path = f"./input/video.mp4"
    path = get_audio(video_path)
    print(path)


@app.command()
def transcribe():
    file_path = "./input/audio.wav"
    transcript = get_transcribe(file_path, "large")
    path = f"./{output_dir}/transcript.txt"
    with open(path, "w") as file:
        file.write(transcript)
        print(transcript)


@app.command()
def summary(path: str):
    file = open(f"./{path}/transcript.txt", "r+")
    transcript = file.read()
    summary = summary_chain.invoke(transcript)
    path = f"./{path}/summarize.txt"
    with open(path, "w") as file:
        file.write(summary)
        print(summary)


@app.command()
def youtube(path: str):
    file = open(f"./{path}/summarize.txt", "r+")
    summary = file.read()
    result = youtube_chain.invoke({"summary": summary, "language": "Spanish"})
    path = f"./{path}/youtube.txt"
    with open(path, "w") as file:
        file.write(result)
        print(result)


@app.command()
def thread(path: str):
    file = open(f"./{path}/summarize.txt", "r+")
    text = file.read()
    paragraphs = list(filter(lambda x: x != "", text.split("\n")))
    result = thread_chain.invoke(
        {
            "word_count": 140,
            "target_audience": "Angular Developers",
            "language": "Spanish",
            "number_of_tweets": len(paragraphs),
            "text": text,
        }
    )
    path = f"./{path}/thread.txt"
    with open(path, "w") as file:
        file.write(result)
        print(result)


@app.command()
def dalle(path: str):
    file = open("./output/summarize.txt", "r+")
    text = file.read()
    response = dalle_chain.invoke(text)
    with open("./output/dalle-prompts.txt", "w") as file:
        file.write(response)
        print(response)


@app.command()
def image():
    file = open("./output/dalle-prompts.txt", "r+")
    text = file.read()
    parts = list(filter(None, text.split("\n")))
    for index, item in enumerate(parts):
        response = generate_image(item, index)
        print(response)


if __name__ == "__main__":
    app()
