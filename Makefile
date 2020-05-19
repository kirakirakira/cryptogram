init:
	pipenv install

activate:
	pipenv shell

test:
	python3 -m unittest -v tests.test_game

run:
	python3 game/game.py
