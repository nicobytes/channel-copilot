include .env

run:
	python main.py summary 
	python main.py audio
	python main.py transcribe ./data/2024-09-06-private
	python main.py summary ./data/2024-09-06-private
	python main.py youtube ./data/2024-09-06-private
	python main.py tweet ./data/2024-09-06-private https://youtu.be/mmQ_I5znuB0 "Developers"
	python main.py thread ./data/2024-09-06-private https://youtu.be/mmQ_I5znuB0 "Developers"
	python main.py linkedin ./data/2024-09-06-private https://youtu.be/mmQ_I5znuB0 "Developers" "text" "video"
	python