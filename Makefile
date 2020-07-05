init:
	pipenv install

activate:
	pipenv shell

test:
	python3 -m unittest -v test_puzzle

coverage_test:
	coverage run -m unittest discover

coverage_report:
	coverage report -m

run:
	python3 game.py
