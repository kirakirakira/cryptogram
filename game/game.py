import re
import random

puzzle = "I am going to play this game"
random_number = random.randint(1, 26)
print(random_number)
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', \
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', \
        'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
original_alphabet = list.copy(alphabet)
random.shuffle(alphabet)

key = {original_alphabet[i]: alphabet[i] for i in range(len(original_alphabet))}

def get_start():
    response = input("Do you want to play? (y/n) ")
    if response.lower() == "y":
        return "Let's play!"
    else:
        return "See you later!"

def get_puzzle():
    transformed_puzzle = "     ".join(puzzle.split())
    transformed_puzzle = re.sub("[a-zA-Z]", "_ ", transformed_puzzle)
    return transformed_puzzle

def play_game():
    print(get_start())
    print(get_puzzle())
    print()


if __name__ == '__main__':
    play_game()