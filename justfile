set dotenv-load

run:
    echo $FOLDER
    echo $YOUTUBE_LINK
    cd app && python main.py audio
    cd app && python main.py transcribe $FOLDER
    cd app && python main.py summary $FOLDER

audio:
    echo $FOLDER
    cd app && python main.py audio

transcribe:
    echo $FOLDER
    cd app && python main.py transcribe $FOLDER

summary:
    cd app && python main.py summary $FOLDER
