# Channel Copilot

Pipeline para transformar un video de YouTube en activos de contenido para redes sociales:

- transcripcion (`.txt` y `.srt`)
- resumen
- titulos para YouTube
- descripcion de YouTube
- capitulos para YouTube
- post para X/Twitter
- post para LinkedIn

## Requisitos

- Conda (Miniconda o Anaconda)
- Python 3.11 (gestionado por `env.yml`)
- `ffmpeg` (incluido en el entorno Conda)
- Claves de API para los modelos que uses

## Instalacion

1) Crea el entorno:

```sh
conda env create -f env.yml
```

2) Activa el entorno:

```sh
conda activate channel
```

`env.yml` instala dependencias de Conda + Pip y deja el proyecto en modo editable (`pip install -e .`).

## Configuracion

1) Crea tu `.env` a partir de `.env-example`.

2) Define al menos estas variables:

```env
OPENAI_API_KEY=
DEEPSEEK_API_KEY=
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=
LANGSMITH_TRACING=True
FOLDER=data/2026-04-15-nx
YOUTUBE_LINK=https://youtu.be/EDRzckXBtKs
```

Notas:

- `FOLDER` es la carpeta donde se guardan los resultados.
- `YOUTUBE_LINK` es el video fuente para la descarga.

## Flujo rapido con Just

Desde la raiz del proyecto:

```sh
just run
```

Este comando ejecuta de forma secuencial:

1. `download`
2. `audio`
3. `transcribe`
4. `summary`
5. `yt-title`
6. `yt-description`
7. `yt-chapters`
8. `tweet`
9. `linkedin`

Tambien puedes ejecutar pasos individuales:

```sh
just audio
just transcribe
just summary
just titles
just description
just chapters
just tweet
just linkedin
```

## Comandos CLI (Typer)

Todos estos comandos se ejecutan desde `app/`.

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

Ejemplo:

```sh
cd app
python main.py transcribe data/2026-04-15-nx
python main.py summary data/2026-04-15-nx
python main.py tweet data/2026-04-15-nx https://youtu.be/EDRzckXBtKs "Developers"
```

## Estructura de salida esperada

Para una corrida con `FOLDER=data/2026-04-15-nx`:

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

## Formateo

```sh
just fmt
```