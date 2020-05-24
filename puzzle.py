import re
import random

puzzle = "I am going to play this game"

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
original_alphabet = list.copy(alphabet)
random.shuffle(alphabet)

key = {original_alphabet[i]: alphabet[i]
       for i in range(len(original_alphabet))}

guesses = {original_alphabet[i]: '' for i in range(len(original_alphabet))}

# print(f'key is {key}')
# print(f'guesses are {guesses}')

guesses['A'] = 'B'

# print(f'guesses are {guesses}')


def are_guesses_correct(key, guesses):
    return key == guesses

# print(are_guesses_correct(key, guesses))
# print(are_guesses_correct(key, key))


hashed_puzzle = ""

for letter in puzzle:
    if letter.isspace():
        hashed_puzzle += letter
    else:
        hashed_puzzle += key[letter.upper()]

transformed_puzzle = "   ".join(puzzle.split())
transformed_puzzle = re.sub("[a-zA-Z]", "_", transformed_puzzle)

hashed_puzzle = "   ".join(hashed_puzzle.split())

# print(transformed_puzzle)
# print(hashed_puzzle)


class Puzzle:
    ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    PUZZLES = ["I am going to play this game",
               "I am going to win this game", "You are going to lose"]

    def __init__(self):
        self.key = dict()
        self.guesses = {Puzzle.ALPHABET[i]                        : '' for i in range(len(Puzzle.ALPHABET))}
        self.puzzle = ""

    def get_key(self):
        original_alphabet = list.copy(Puzzle.ALPHABET)
        random.shuffle(original_alphabet)
        self.key = {Puzzle.ALPHABET[i]: original_alphabet[i]
                    for i in range(len(Puzzle.ALPHABET))}
        # print(self.key)

    def get_puzzle(self):
        self.puzzle = random.choice(Puzzle.PUZZLES)
        # print(self.puzzle)

    def display_puzzle(self):
        hashed_puzzle = ""
        for letter in self.puzzle:
            if letter.isspace():
                hashed_puzzle += letter
            else:
                hashed_puzzle += self.key[letter.upper()]

        transformed_puzzle = "   ".join(self.puzzle.split())
        transformed_puzzle = re.sub("[a-zA-Z]", "_", transformed_puzzle)

        hashed_puzzle = "   ".join(hashed_puzzle.split())

        print(transformed_puzzle)
        print(hashed_puzzle)

puzzle = Puzzle()
puzzle.get_key()
puzzle.get_puzzle()
puzzle.display_puzzle()