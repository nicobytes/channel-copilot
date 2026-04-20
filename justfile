set dotenv-load

fmt:
    ruff format app

check:
    ruff check app

lint:
    ruff check app

lint-fix:
    ruff check --fix app

format:
    ruff format app

run:
    echo $FOLDER
    echo $YOUTUBE_LINK
    cd app && python main.py download $YOUTUBE_LINK --quality lowest
    cd app && python main.py audio
    cd app && python main.py transcribe $FOLDER
    cd app && python main.py summary $FOLDER
    cd app && python main.py yt-title $FOLDER "Spanish LATAM"
    cd app && python main.py yt-description $FOLDER "Spanish LATAM"
    cd app && python main.py yt-chapters $FOLDER "Spanish LATAM"
    cd app && python main.py tweet $FOLDER $YOUTUBE_LINK "Developers"
    cd app && python main.py linkedin $FOLDER "Spanish LATAM"

download:
    echo "Downloading video..."
    echo $FOLDER
    cd app && python main.py download https://www.youtube.com/watch?v=ILuVtpnWZNU --quality highest

audio:
    echo $FOLDER
    cd app && python main.py audio

transcribe:
    echo $FOLDER
    cd app && python main.py transcribe $FOLDER

summary:
    echo $FOLDER
    cd app && python main.py summary $FOLDER

youtube-titles:
    echo $FOLDER
    cd app && python main.py yt-title $FOLDER "Spanish LATAM"

youtube-description:
    echo $FOLDER
    cd app && python main.py yt-description $FOLDER "Spanish LATAM"

youtube-chapters:
    echo $FOLDER
    cd app && python main.py yt-chapters $FOLDER "Spanish LATAM"

# Backward-compatible aliases.
titles:
    @just youtube-titles

description:
    @just youtube-description

chapters:
    @just youtube-chapters

tweet:
    echo $FOLDER
    echo $YOUTUBE_LINK
    cd app && python main.py tweet $FOLDER $YOUTUBE_LINK "Developers"

linkedin:
    echo $FOLDER
    cd app && python main.py linkedin $FOLDER "Spanish LATAM"