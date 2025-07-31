set dotenv-load

run:
    echo $FOLDER
    echo $YOUTUBE_LINK
    python main.py audio
    python main.py transcribe $FOLDER
    python main.py summary $FOLDER
    python main.py youtube $FOLDER
    python main.py tweet $FOLDER $YOUTUBE_LINK "Developers"
    python main.py thread $FOLDER $YOUTUBE_LINK "Developers"
    python main.py linkedin $FOLDER $YOUTUBE_LINK "Developers" "text" "video"

audio:
    echo $FOLDER
    cd app && python main.py audio

transcribe:
    echo $FOLDER
    cd app && python main.py transcribe $FOLDER

summary:
    cd app && python main.py summary $FOLDER
