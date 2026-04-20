from pathlib import Path
from typing import Literal

from pytubefix import YouTube


def _resolution_height(stream) -> int:
    resolution = getattr(stream, "resolution", None) or ""
    if not resolution.endswith("p"):
        return 0
    value = resolution[:-1]
    return int(value) if value.isdigit() else 0


def download_video(
    video_url: str, output_path: str, preferred_resolution: Literal["lowest", "highest"]
) -> str:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    try:
        yt = YouTube(video_url)
    except Exception as error:
        raise RuntimeError(
            "Could not initialize the video download. "
            "Make sure the URL is public and valid."
        ) from error
    if preferred_resolution == "highest":
        stream = (
            yt.streams.filter(adaptive=True, only_video=True, file_extension="mp4")
            .order_by("resolution")
            .desc()
            .first()
        )
        if stream is None or _resolution_height(stream) < 1080:
            raise ValueError(
                "No video-only MP4 stream with a minimum resolution of 1080p was found."
            )
    else:
        stream = yt.streams.get_lowest_resolution()

    if stream is None:
        raise ValueError("No compatible stream was found for download.")

    try:
        stream.download(output_path=str(path.parent), filename=path.name)
    except Exception as error:
        raise RuntimeError(
            "The video could not be downloaded from YouTube at this time."
        ) from error
    return str(path)
