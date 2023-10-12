# Create env

```sh
conda env create -f environment.yml
```

# Activate env

```sh
conda activate notebooks
```

# Install deps

```sh
poetry install
```

# Generate conda env from zero
```sh
conda create --name notebooks python=3.10
conda activate notebooks
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
conda install -c conda-forge poetry
conda install -c conda-forge ffmpeg
conda env export > environment.yml
poetry init
```

# Run
```py
python main.py audio
python main.py transcribe
python main.py summary
python main.py tweet
python main.py dalle
python main.py image
``` 

# TODOs

- [ ] Avoid be rebudant
- [ ] change aprenderemos por aprenderás
- [ ] improvements in generate tweets with summary, hasttags, include links, emojis etc
- [ ] test generate images