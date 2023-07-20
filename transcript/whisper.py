import whisper

def get_transcribe(path, type="base"):
  model = whisper.load_model(type)
  result = model.transcribe(path, fp16=False, language="es")
  return result

def write_transcribe(path, type="base"):
  result = get_transcribe(path, type)
  text = result.get('text', '')
  with open('./data/transcript.txt', 'w') as file:
    file.write(text)
  return True