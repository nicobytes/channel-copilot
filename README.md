# Create env

```sh
conda env create -f environment.yml
```

# Activate env

```sh
conda activate channel
```

# Install deps

```sh
poetry install
```

# Generate conda env from zero
```sh
conda create --name channel python=3.10
conda activate channel
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
conda install -c conda-forge poetry
conda install -c conda-forge ffmpeg
conda env export > environment.yml
poetry init

```

# Run
```py
python main.py audio
python main.py transcribe ./data/2025-05-13-ux
python main.py summary ./data/2025-05-13-ux
python main.py youtube ./data/2025-05-13-ux
python main.py tweet ./data/2025-05-13-ux https://youtu.be/3XEQhMu3g6k "Developers"
python main.py linkedin ./data/2025-05-13-ux https://youtu.be/3XEQhMu3g6k "Developers" "text" "video"
python main.py thread ./data/2025-05-13-ux https://youtu.be/OAU1uHgg8GY "Developers"
python main.py blog ./data/2025-05-13-ux  
``` 

# TODOs

- [ ] Avoid be rebudant
- [ ] change aprenderemos por aprenderás
- [ ] improvements in generate tweets with summary, hasttags, include links, emojis etc
- [ ] test generate images
- [ ] chain to generate title, description and keywords


04:05 gemma onic
30:27 conductio