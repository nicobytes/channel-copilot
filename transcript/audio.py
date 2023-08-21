import moviepy.editor as mp

def get_audio_from_mp4(name, path_file):
    video = mp.VideoFileClip(path_file)
    audio = video.audio
    audio_path = f"./input/{name}.wav"
    audio.write_audiofile(audio_path)
    return audio_path

def get_audio():
    video_path = f"./input/video.mp4"
    path_audio = get_audio_from_mp4('video', video_path)
    return path_audio