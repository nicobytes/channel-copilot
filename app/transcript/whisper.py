import whisper
from whisper.utils import get_writer

def get_transcribe(path, type="base"):
    model = whisper.load_model(type)
    results = model.transcribe(path, fp16=False, language="es", verbose=True)
    return results

def save_file(results, path, format='txt'):
    writer = get_writer(format, path)
    writer(results, f'transcript.{format}')
    
