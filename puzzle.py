import re
import random

# puzzle = "I am going to play this game"

# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
#             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
#             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# original_alphabet = list.copy(alphabet)
# random.shuffle(alphabet)

# key = {original_alphabet[i]: alphabet[i]
#        for i in range(len(original_alphabet))}

# guesses = {original_alphabet[i]: '' for i in range(len(original_alphabet))}

# # print(f'key is {key}')
# # print(f'guesses are {guesses}')

# guesses['A'] = 'B'

# # print(f'guesses are {guesses}')


# def are_guesses_correct(key, guesses):
#     return key == guesses

# # print(are_guesses_correct(key, guesses))
# # print(are_guesses_correct(key, key))


# hashed_puzzle = ""

# for letter in puzzle:
#     if letter.isspace():
#         hashed_puzzle += letter
#     else:
#         hashed_puzzle += key[letter.upper()]

# transformed_puzzle = "   ".join(puzzle.split())
# transformed_puzzle = re.sub("[a-zA-Z]", "_", transformed_puzzle)

# hashed_puzzle = "   ".join(hashed_puzzle.split())

# # print(transformed_puzzle)
# # print(hashed_puzzle)


class Puzzle:
    ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    PUZZLES = ["I am going to play this game",
               "I am going to win this game", "You are going to lose"]

    def __init__(self):
        self.hashed_key = dict()
        self.guesses = {
            Puzzle.ALPHABET[i]: '_' for i in range(len(Puzzle.ALPHABET))}
        self.puzzle = ""
        self.hashed_puzzle = ""
        self.updated_puzzle = ""

    def get_key(self):
        original_alphabet = list.copy(Puzzle.ALPHABET)
        random.shuffle(original_alphabet)
        self.hashed_key = {Puzzle.ALPHABET[i]: original_alphabet[i]
                                  for i in range(len(Puzzle.ALPHABET))}

    def get_puzzle(self):
        self.puzzle = random.choice(Puzzle.PUZZLES)

    def hash_the_puzzle(self):
        for letter in self.puzzle:
            if letter.isspace():
                self.hashed_puzzle += letter
            else:
                self.hashed_puzzle += self.hashed_key[letter.upper()]

        self.hashed_puzzle = "   ".join(self.hashed_puzzle.split())

    def display_puzzle(self):
        print(self.updated_puzzle)
        print(self.hashed_puzzle)

    def guess_a_letter(self, letter_to_replace, letter_to_replace_with):
        self.guesses[letter_to_replace] = letter_to_replace_with

        self.updated_puzzle = ""
        for letter in self.hashed_puzzle:
            if letter.isspace():
                    self.updated_puzzle += letter
            else:
                    self.updated_puzzle += self.guesses[letter.upper()]

    def puzzle_matches_key(self):
        return self.guesses == self.hashed_key

puzzle = Puzzle()
puzzle.get_key()
puzzle.get_puzzle()
puzzle.hash_the_puzzle()
puzzle.guess_a_letter('A', 'C')
puzzle.guess_a_letter('B', 'D')
puzzle.guess_a_letter('E', 'O')
puzzle.guess_a_letter('I', 'B')
puzzle.display_puzzle()
