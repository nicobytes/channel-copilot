import typer
from transcript.audio import get_audio
from transcript.whisper import write_transcribe
from chains.summary_chain import SummaryChain
from chains.twets_chain import TweetsChain
from image.image import generate_image
import settings
from rich import print

app = typer.Typer()


@app.command()
def audio():
    path = get_audio()
    print(path)


@app.command()
def transcribe():
    transcript = write_transcribe('./data/video.mp4', 'large')
    print(transcript)


@app.command()
def summary():
    summary_chain = SummaryChain.from_class()
    file = open("./data/transcript.txt", "r+")
    transcript = file.read()
    summary = summary_chain.generate_response(transcript=transcript)
    with open('./data/summarize.txt', 'w') as file:
        file.write(summary)
        print(summary)


@app.command()
def tweets():
    tweets_chain = TweetsChain.from_class()
    file = open("./data/summarize.txt", "r+")
    context = file.read()
    tweets = tweets_chain.generate_response(context=context)
    with open('./data/tweets.txt', 'w') as file:
        file.write(tweets)
        print(tweets)


@app.command()
def image():
    generate_image("An dog in the middle of the forest")


if __name__ == "__main__":
    app()