import re

puzzle = "I am going to play this game"

def get_start():
    response = input("Do you want to play? (y/n) ")
    if response.lower() == "y":
        return "Let's play!"
    else:
        return "See you later!"

def print_puzzle():
    transformed_puzzle = "     ".join(puzzle.split())
    transformed_puzzle = re.sub("[a-zA-Z]", "_ ", transformed_puzzle)
    return transformed_puzzle

def play_game():
    response = get_start()
    print(response)
    if response == "Let's play!":
        print(print_puzzle())
        print()

play_game()