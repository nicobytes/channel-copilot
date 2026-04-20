# Channel Copilot

Pipeline to transform a YouTube video into social media content assets:

- transcription (`.txt` and `.srt`)
- summary
- YouTube titles
- YouTube description
- YouTube chapters
- X/Twitter post
- LinkedIn post

## Requirements

- Conda (Miniconda or Anaconda)
- Python 3.11 (managed by `env.yml`)
- `ffmpeg` (included in the Conda environment)
- API keys for the models you use

## Installation

1) Create the environment:

```sh
conda env create -f env.yml
```

2) Activate the environment:

```sh
conda activate channel
```

`env.yml` installs Conda + Pip dependencies and sets the project in editable mode (`pip install -e .`).

## Configuration

1) Create your `.env` file from `.env-example`.

2) Define at least these variables:

```env
OPENAI_API_KEY=
DEEPSEEK_API_KEY=
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=
LANGSMITH_TRACING=True
FOLDER=data/2026-04-15-nx
YOUTUBE_LINK=https://youtu.be/EDRzckXBtKs
```

Notes:

- `FOLDER` is the directory where outputs are written.
- `YOUTUBE_LINK` is the source video URL to download.

## Quick Flow with Just

From the project root:

```sh
just run
```

This command runs the following steps sequentially:

1. `download`
2. `audio`
3. `transcribe`
4. `summary`
5. `yt-title`
6. `yt-description`
7. `yt-chapters`
8. `tweet`
9. `linkedin`

You can also run individual steps:

```sh
just audio
just transcribe
just summary
just youtube-titles
just youtube-description
just youtube-chapters
just tweet
just linkedin
```

## CLI Commands (Typer)

All commands below are run from `app/`.

```sh
python main.py download <video_url>
python main.py audio
python main.py transcribe <path>
python main.py summary <path>
python main.py yt-title <path> "Spanish LATAM"
python main.py yt-description <path> "Spanish LATAM"
python main.py yt-chapters <path> "Spanish LATAM"
python main.py tweet <path> <youtube_link> "Developers"
python main.py linkedin <path> "Spanish LATAM"
```

Example:

```sh
cd app
python main.py transcribe data/2026-04-15-nx
python main.py summary data/2026-04-15-nx
python main.py tweet data/2026-04-15-nx https://youtu.be/EDRzckXBtKs "Developers"
```

## Expected Output Structure

For a run with `FOLDER=data/2026-04-15-nx`:

```text
app/data/2026-04-15-nx/
  transcript.txt
  transcript.srt
  summarize.md
  yt_titles.md
  yt_description.md
  yt_chapters.md
  tweet.md
  linkedin.md
```

## Formatting and Linting

```sh
just fmt
just lint
```