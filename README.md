# Cryptogram
Cryptogram puzzle game in Python

This is a Cryptogram puzzle game that you can play in the console.

## How to run
0. Must have [Python 3.8](https://www.python.org/downloads/) and pipenv installed ([installation instructions](https://pypi.org/project/pipenv/))
1. Clone this repo: `git clone https://github.com/kirakirakira/cryptogram.git`
2. Make sure you are in the top project directory (cryptogram if you didn't rename it)
2. Run `make init` to install dependencies.
3. Run `make activate` to activate the virtual environment.
4. Run `make run` to start the game.

## How to run tests
1. Run `make test_puzzle` to run tests on `Puzzle`.
2. Run `make test_game` to run tests on `Game`.

## Game Overview
This is a Cryptogram puzzle game, and you will be deciphering some text and that text is a title of an episode of Gilmore Girls. For more on [Cryptograms](https://en.wikipedia.org/wiki/Cryptogram). For a list of Gilmore Girl [episodes](https://en.wikipedia.org/wiki/List_of_Gilmore_Girls_episodes).

Since the game can take a while to actually play, you might notice that the answer is printed out at the beginning of a round of play...obviously this is just for testing purposes. :satisfied:

```
Do you want to play? (y/n) y
Let's play!

"The  Great  Stink"

What difficulty would you like to play? (easy (E)/medium (M)/hard (H)) H
Number of turns: 10
"___  _____  _____"
"AZS  LYSRA  OAVJQ"
What letter would you like to replace? A
What letter would you like to replace it with? T
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    
Turns left: 9

"T__  ____T  _T___"
"AZS  LYSRA  OAVJQ"
What letter would you like to replace? 
```

## Project Requirements Met
- Implemented a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program (`play_game` and `play_round`)
- Created a class, then created at least one object of that class and populate it with data (`Puzzle`'s puzzles come from `Soup`)
- Created a dictionary or list, populated it with several values, retrieved at least one value, and used it in the program (`self.alpha_to_hash`, `self.hash_to_alpha`, and `self.alpha_to_guesses`)
- Read data from an external file, such as text, JSON, CSV, etc and use that data in your application (scraped a webpage using Beautiful Soup) (`Soup` scrapes Gilmore Girl episode titles from a Wikipedia page)
- Created and called at least 3 functions, at least one of which returned a value that is used (there's a whole bunch)
- Create 3 or more unit tests for your application (see `test_game.py` and `test_puzzle.py`)

## Other Requirements
- Comments exist
- > 70 commits

