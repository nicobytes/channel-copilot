set dotenv-load

fmt:
    black app

run:
    echo $FOLDER
    echo $YOUTUBE_LINK
    echo $LANGSMITH_API_KEY
    cd app && python main.py download $YOUTUBE_LINK
    cd app && python main.py audio
    cd app && python main.py transcribe $FOLDER
    cd app && python main.py summary $FOLDER
    cd app && python main.py yt-title $FOLDER "Spanish LATAM"
    cd app && python main.py yt-description $FOLDER "Spanish LATAM"
    cd app && python main.py yt-chapters $FOLDER "Spanish LATAM"
    cd app && python main.py tweet $FOLDER $YOUTUBE_LINK "Developers"
    cd app && python main.py linkedin $FOLDER "Spanish LATAM"

audio:
    echo $FOLDER
    cd app && python main.py audio

transcribe:
    echo $FOLDER
    cd app && python main.py transcribe $FOLDER

summary:
    echo $FOLDER
    cd app && python main.py summary $FOLDER

titles:
    echo $FOLDER
    cd app && python main.py yt-title $FOLDER "Spanish LATAM"

description:
    echo $FOLDER
    cd app && python main.py yt-description $FOLDER "Spanish LATAM"

chapters:
    echo $FOLDER
    cd app && python main.py yt-chapters $FOLDER "Spanish LATAM"

tweet:
    echo $FOLDER
    echo $YOUTUBE_LINK
    cd app && python main.py tweet $FOLDER $YOUTUBE_LINK "Developers"

linkedin:
    echo $FOLDER
    cd app && python main.py linkedin $FOLDER "Spanish LATAM"