from moviepy import VideoFileClip


def get_audio(path_file):
    video = VideoFileClip(path_file)
    audio = video.audio
    audio_path = f"./input/audio.wav"
    audio.write_audiofile(audio_path)
    return audio_path
