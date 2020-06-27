init:
	pipenv install

activate:
	pipenv shell

test:
	python3 -m unittest -v test_puzzle

run:
	python3 game.py
