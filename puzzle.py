import re
import random

from trumpograms.trumpdump import Dump


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
        self.dump = Dump()
        self.puzzles = self.dump.get_tweets()

    def reset_puzzle(self):
        self.guesses = {
            Puzzle.ALPHABET[i]: '_' for i in range(len(Puzzle.ALPHABET))}
        self.puzzle = ""
        self.hashed_puzzle = ""
        self.updated_puzzle = ""
        self.answer_puzzle = ""

    def get_key(self):
        original_alphabet = list.copy(Puzzle.ALPHABET)
        random.shuffle(original_alphabet)
        self.hashed_key_forwards = {Puzzle.ALPHABET[i]: original_alphabet[i]
                                    for i in range(len(Puzzle.ALPHABET))}
        self.hashed_key_backwards = {original_alphabet[i]: Puzzle.ALPHABET[i]
                                     for i in range(len(Puzzle.ALPHABET))}

    def get_puzzle(self):
        self.puzzle = random.choice(self.puzzles)

    def hash_the_puzzle(self):
        for letter in self.puzzle:
            if letter.isspace():
                self.hashed_puzzle += letter
            elif letter.upper() in Puzzle.ALPHABET: # need to only do this for letters and skip special characters
                self.hashed_puzzle += self.hashed_key_backwards[letter.upper()]

        self.hashed_puzzle = "   ".join(self.hashed_puzzle.split())

    def update_puzzle(self):
        self.updated_puzzle = ""
        for letter in self.hashed_puzzle:
            if letter.isspace():
                self.updated_puzzle += letter
            else:
                self.updated_puzzle += self.guesses[letter.upper()]

    def get_answer_puzzle(self):
        self.answer_puzzle = ""
        for letter in self.puzzle:
            if letter.isspace():
                self.answer_puzzle += letter
            elif letter.upper() in Puzzle.ALPHABET:
                self.answer_puzzle += letter.upper()
        self.answer_puzzle = "   ".join(self.answer_puzzle.split())
        return self.answer_puzzle

    def display_puzzle(self):
        print(self.updated_puzzle)
        print(self.hashed_puzzle)

    def set_guesses_equal_to_key(self):
        self.guesses = self.hashed_key_forwards

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
