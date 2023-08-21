import typer
from transcript.audio import get_audio
from transcript.whisper import write_transcribe
from chains.summary_chain import SummaryChain
from chains.twets_chain import TweetsChain
from chains.dalle_chain import DalleChain
from image.dalle import generate_image
#from image.stable_diffusion import generate_image
import settings
from rich import print

app = typer.Typer()


@app.command()
def audio():
    path = get_audio()
    print(path)


@app.command()
def transcribe():
    transcript = write_transcribe('./input/video.mp4', 'large')
    print(transcript)


@app.command()
def summary():
    summary_chain = SummaryChain.from_class()
    file = open("./output/transcript.txt", "r+")
    transcript = file.read()
    summary = summary_chain.generate_response(transcript=transcript)
    with open('./output/summarize.txt', 'w') as file:
        file.write(summary)
        print(summary)


@app.command()
def tweets():
    tweets_chain = TweetsChain.from_class()
    file = open("./output/summarize.txt", "r+")
    context = file.read()
    tweets = tweets_chain.generate_response(context=context)
    with open('./output/tweets.txt', 'w') as file:
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