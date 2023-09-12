import typer
from transcript.audio import get_audio
from transcript.whisper import get_transcribe
from chains.summary_chain import SummaryChain
from chains.twet_chain import TweetChain
from chains.dalle_chain import DalleChain
from image.dalle import generate_image
#from image.stable_diffusion import generate_image
import settings
from rich import print

app = typer.Typer()
output_dir = './data/2023-09-12-standalone'


@app.command()
def audio():
    video_path = f"./input/video.mp4"
    path = get_audio(video_path)
    print(path)


@app.command()
def transcribe():
    file_path = './input/audio.wav'
    transcript = get_transcribe(file_path, 'large')
    path = f'./{output_dir}/transcript.txt'
    with open(path, 'w') as file:
        file.write(transcript)
        print(transcript)


@app.command()
def summary():
    summary_chain = SummaryChain.from_class()
    file = open(f"./{output_dir}/transcript.txt", "r+")
    transcript = file.read()
    summary = summary_chain.generate_response(transcript=transcript)
    path = f'./{output_dir}/summarize.txt'
    with open(path, 'w') as file:
        file.write(summary)
        print(summary)


@app.command()
def tweet():
    tweet_chain = TweetChain.from_class()
    file = open(f"./{output_dir}/summarize.txt", "r+")
    summary = file.read()
    tweets = tweet_chain.generate_response(summary=summary)
    path = f'./{output_dir}/tweet.txt'
    with open(path, 'w') as file:
        file.write(tweets)
        print(tweets)


@app.command()
def dalle():
    chain = DalleChain.from_class()
    file = open("./output/summarize.txt", "r+")
    text = file.read()
    response = chain.generate_response(text=text)
    with open('./output/dalle-prompts.txt', 'w') as file:
        file.write(response)
        print(response)


@app.command()
def image():
    file = open("./output/dalle-prompts.txt", "r+")
    text = file.read()
    parts = list(filter(None, text.split('\n')))
    for index, item in enumerate(parts):
        response = generate_image(item, index)
        print(response)

if __name__ == "__main__":
    app()