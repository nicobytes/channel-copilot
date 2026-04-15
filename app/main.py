from settings import settings
import importlib.util
import time
from pathlib import Path
import typer
from transcript.audio import get_audio
from transcript.video import download_video
from transcript.whisper import get_transcribe, save_file
from agents.summarize.agent import summarize_transcript
from agents.tweet.agent import create_tweet
from agents.linkedin.agent import create_linkedin_post
from agents.yt_title.agent import create_titles
from agents.yt_description.agent import create_description
from rich import print
from rich.progress import track

app = typer.Typer()


def _load_create_chapters():
    agent_path = Path(__file__).resolve().parent / "agents" / "yt-chapters" / "agent.py"
    spec = importlib.util.spec_from_file_location("yt_chapters_agent", agent_path)
    if spec is None or spec.loader is None:
        raise ImportError("Unable to load yt-chapters agent module.")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    create_chapters = getattr(module, "create_chapters", None)
    if create_chapters is None:
        raise ImportError("yt-chapters agent does not expose create_chapters.")

    return create_chapters


create_chapters = _load_create_chapters()


@app.command()
def download(video_url: str):
    output_path = "./input/video.mp4"
    print(f"Descargando video desde: {video_url}")
    path = download_video(video_url, output_path)
    print(f"Video guardado en: {path}")


@app.command()
def audio():
    video_path = f"./input/video.mp4"
    path = get_audio(video_path)
    print(path)


@app.command()
def transcribe(path: str):
    file_path = "./input/audio.wav"
    results = get_transcribe(file_path, "large")
    save_file(results, f"./{path}", "txt")
    save_file(results, f"./{path}", "srt")


@app.command()
def summary(path: str):
    start_time = time.time()
    transcript_path = f"./{path}/transcript.txt"
    output_path = f"./{path}/summarize.md"

    print(f"[cyan]Starting summary for:[/cyan] {transcript_path}")

    for _ in track(range(1), description="Reading transcript..."):
        time.sleep(0.01)
        with open(transcript_path, "r+", encoding="utf-8") as file:
            transcript = file.read()

    for _ in track(range(1), description="Generating summary with Deep Agent..."):
        summary = summarize_transcript(transcript)

    for _ in track(range(1), description="Saving summary..."):
        time.sleep(0.01)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(summary)

    elapsed = time.time() - start_time
    print(f"[green]Summary saved:[/green] {output_path}")
    print(f"[yellow]Elapsed:[/yellow] {elapsed:.2f}s")
    print(summary)


@app.command()
def yt_title(path: str, language: str):
    file = open(f"./{path}/summarize.md", "r+", encoding="utf-8")
    summary = file.read()
    result = create_titles(summary, language)
    output_path = f"./{path}/yt_titles.md"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(result)
        print(result)


@app.command()
def yt_description(path: str, language: str):
    file = open(f"./{path}/summarize.md", "r+", encoding="utf-8")
    summary = file.read()
    result = create_description(summary, language)
    output_path = f"./{path}/yt_description.md"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(result)
        print(result)


@app.command()
def yt_chapters(path: str, language: str):
    with open(f"./{path}/transcript.srt", "r+", encoding="utf-8") as file:
        transcript = file.read()
    with open(f"./{path}/summarize.md", "r+", encoding="utf-8") as file:
        summary = file.read()

    result = create_chapters(transcript, summary, language)
    output_path = f"./{path}/yt_chapters.md"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(result)
        print(result)


@app.command()
def tweet(path: str, link: str, target: str):
    with open(f"./{path}/summarize.md", "r+", encoding="utf-8") as file:
        summary = file.read()
    result = create_tweet(summary, "Spanish LATAM", target, link)
    output_path = f"./{path}/tweet.md"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(result)
        print(result)


@app.command()
def linkedin(path: str, language: str):
    file = open(f"./{path}/summarize.md", "r+", encoding="utf-8")
    summary = file.read()
    result = create_linkedin_post(summary, language)
    output_path = f"./{path}/linkedin.md"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(result)
        print(result)


if __name__ == "__main__":
    app()
