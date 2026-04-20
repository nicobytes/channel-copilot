import time
from typing import Literal

import typer
from agents.linkedin.agent import create_linkedin_post
from agents.summarize.agent import summarize_transcript
from agents.tweet.agent import create_tweet
from agents.yt_chapters.agent import create_chapters
from agents.yt_description.agent import create_description
from agents.yt_title.agent import create_titles
from rich import print
from rich.progress import track
from transcript.audio import get_audio
from transcript.video import download_video
from transcript.whisper import get_transcribe, save_file

app = typer.Typer()


@app.command("download")
def download_video_command(
    video_url: str,
    quality: Literal["lowest", "highest"] = typer.Option(
        ...,
        "--quality",
        "-q",
        help="Required quality. Allowed values: lowest or highest.",
    ),
):
    output_path = "./input/video.mp4"
    print(f"Downloading video from: {video_url}")
    print(f"Selected quality: {quality}")
    path = download_video(video_url, output_path, quality)
    print(f"Video saved to: {path}")


@app.command("audio")
def extract_audio_command():
    video_path = "./input/video.mp4"
    path = get_audio(video_path)
    print(path)


@app.command("transcribe")
def transcribe_command(path: str):
    file_path = "./input/audio.wav"
    results = get_transcribe(file_path, "large")
    save_file(results, f"./{path}", "txt")
    save_file(results, f"./{path}", "srt")


@app.command("summary")
def summarize_command(path: str):
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


@app.command("yt-title")
def youtube_title_command(path: str, language: str):
    file = open(f"./{path}/summarize.md", "r+", encoding="utf-8")
    summary = file.read()
    result = create_titles(summary, language)
    output_path = f"./{path}/yt_titles.md"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(result)
        print(result)


@app.command("yt-description")
def youtube_description_command(path: str, language: str):
    file = open(f"./{path}/summarize.md", "r+", encoding="utf-8")
    summary = file.read()
    result = create_description(summary, language)
    output_path = f"./{path}/yt_description.md"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(result)
        print(result)


@app.command("yt-chapters")
def youtube_chapters_command(path: str, language: str):
    with open(f"./{path}/transcript.srt", "r+", encoding="utf-8") as file:
        transcript = file.read()
    with open(f"./{path}/summarize.md", "r+", encoding="utf-8") as file:
        summary = file.read()

    result = create_chapters(transcript, summary, language)
    output_path = f"./{path}/yt_chapters.md"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(result)
        print(result)


@app.command("tweet")
def tweet_command(path: str, link: str, target: str):
    with open(f"./{path}/summarize.md", "r+", encoding="utf-8") as file:
        summary = file.read()
    result = create_tweet(summary, "Spanish LATAM", target, link)
    output_path = f"./{path}/tweet.md"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(result)
        print(result)


@app.command("linkedin")
def linkedin_command(path: str, language: str):
    file = open(f"./{path}/summarize.md", "r+", encoding="utf-8")
    summary = file.read()
    result = create_linkedin_post(summary, language)
    output_path = f"./{path}/linkedin.md"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(result)
        print(result)


if __name__ == "__main__":
    app()
