# Create env

```sh
conda env create -f environment.yml
conda activate channel
```

# Install poetry

```sh
pip install poetry
poetry install
```

# Run
```py
python main.py audio
python main.py transcribe
python main.py summary
python main.py tweets
python main.py image
``` 

# Generate conda env
```sh
conda create --name channel python=3.10
conda pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
conda install -c conda-forge poetry
conda install -c conda-forge ffmpeg
conda env export > environment.yml
```