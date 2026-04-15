from pathlib import Path

from pytubefix import YouTube


def download_video(video_url: str, output_path: str) -> str:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    try:
        yt = YouTube(video_url)
    except Exception as error:
        raise RuntimeError(
            "No se pudo inicializar la descarga del video. "
            "Verifica que la URL sea publica y valida."
        ) from error
    progressive_streams = yt.streams.filter(
        progressive=True, file_extension="mp4"
    ).order_by("resolution")
    # Preferimos 360p para reducir tamaño y facilitar extracción de audio.
    stream = (
        progressive_streams.filter(res="360p").first() or progressive_streams.first()
    )

    if stream is None:
        raise ValueError("No se encontró un stream mp4 progresivo para descargar.")

    try:
        stream.download(output_path=str(path.parent), filename=path.name)
    except Exception as error:
        raise RuntimeError(
            "No se pudo descargar el video desde YouTube en este momento."
        ) from error
    return str(path)
