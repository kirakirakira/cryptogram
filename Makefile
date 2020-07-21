init:
	pipenv install

activate:
	pipenv shell

test_puzzle:
	python3 -m unittest -v test_puzzle

test_game:
	python3 -m unittest -v test_game

coverage_test:
	coverage run -m unittest discover

coverage_report:
	coverage report -m

run:
	python3 game.py
