# Cryptogram
Cryptogram puzzle game in Python

This is a Cryptogram puzzle game that you can play in the console.

## How to run
Must have pipenv installed
1. Clone this repo
2. Make sure you are in the top directory.
2. Run `make init` to install dependencies.
3. Run `make activate` to activate the virtual environment.
4. Run `make run` to start the game.
5. Run `make test` to run tests on `Puzzle`.

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
- Implemented a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
- Created a class, then created at least one object of that class and populate it with data
- Created a dictionary or list, populated it with several values, retrieved at least one value, and used it in the program
- Read data from an external file, such as text, JSON, CSV, etc and use that data in your application (scraped a webpage using Beautiful Soup)
- Created and called at least 3 functions, at least one of which returned a value that is used

