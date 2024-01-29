import whisper


def get_transcribe(path, type="base"):
    model = whisper.load_model(type)
    result = model.transcribe(path, fp16=False, language="es", verbose=True)
    return result.get("text", "")
