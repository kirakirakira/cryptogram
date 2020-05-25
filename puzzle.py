import re
import random


class Puzzle:
    ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    PUZZLES = ["I am",
               "game", "You"]

    def __init__(self):
        self.hashed_key_forwards = dict()
        self.hashed_key_backwards = dict()
        self.guesses = {
            Puzzle.ALPHABET[i]: '_' for i in range(len(Puzzle.ALPHABET))}
        self.puzzle = ""
        self.hashed_puzzle = ""
        self.updated_puzzle = ""

    def reset_puzzle(self):
        self.guesses = {
            Puzzle.ALPHABET[i]: '_' for i in range(len(Puzzle.ALPHABET))}
        self.puzzle = ""
        self.hashed_puzzle = ""
        self.updated_puzzle = ""

    def get_key(self):
        original_alphabet = list.copy(Puzzle.ALPHABET)
        random.shuffle(original_alphabet)
        self.hashed_key_forwards = {Puzzle.ALPHABET[i] : original_alphabet[i]
                                  for i in range(len(Puzzle.ALPHABET))}
        self.hashed_key_backwards = {original_alphabet[i] : Puzzle.ALPHABET[i]
                                  for i in range(len(Puzzle.ALPHABET))}

    def get_puzzle(self):
        self.puzzle = random.choice(Puzzle.PUZZLES)

    def hash_the_puzzle(self):
        for letter in self.puzzle:
            if letter.isspace():
                self.hashed_puzzle += letter
            else:
                self.hashed_puzzle += self.hashed_key_backwards[letter.upper()]

        self.hashed_puzzle = "   ".join(self.hashed_puzzle.split())

    def update_puzzle(self):
        self.updated_puzzle = ""
        for letter in self.hashed_puzzle:
            if letter.isspace():
                self.updated_puzzle += letter
            else:
                self.updated_puzzle += self.guesses[letter.upper()]

    def display_puzzle(self):
        print(self.updated_puzzle)
        print(self.hashed_puzzle)

    def guess_a_letter(self, letter_to_replace, letter_to_replace_with):
        self.guesses[letter_to_replace] = letter_to_replace_with

    def puzzle_matches_key(self):
        for letter in self.hashed_puzzle:
            if not letter.isspace():
                if self.guesses[letter] == self.hashed_key_forwards[letter]:
                    continue
                else:
                    return False
        return True

