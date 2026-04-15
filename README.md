# Create env

```sh
conda env create -f env.yml
```

# Activate env

```sh
conda activate channel
```

# List dependencies

```sh
conda list
```

El `env.yml` instala todas las dependencias (conda + pip) y el proyecto en editable (`pip install -e .`). No hace falta Poetry.

Agrega `YOUTUBE_LINK` en tu archivo `.env` para usar la descarga automática de video.

# Run
```py
python main.py download
python main.py audio
python main.py transcribe ./data/2025-07-03-lint-ci
python main.py summary ./data/2025-07-03-lint-ci
python main.py youtube ./data/2025-07-03-lint-ci
python main.py tweet ./data/2025-07-03-lint-ci https://youtu.be/3XEQhMu3g6k "Developers"
python main.py linkedin ./data/2025-07-03-lint-ci https://youtu.be/3XEQhMu3g6k "Developers" "text" "video"
python main.py thread ./data/2025-07-03-lint-ci https://youtu.be/OAU1uHgg8GY "Developers"
python main.py blog ./data/2025-07-03-lint-ci 
``` 

# TODOs

- [ ] Avoid be rebudant
- [ ] change aprenderemos por aprenderás
- [ ] improvements in generate tweets with summary, hasttags, include links, emojis etc
- [ ] test generate images
- [ ] chain to generate title, description and keywords


04:05 gemma onic
30:27 conductio