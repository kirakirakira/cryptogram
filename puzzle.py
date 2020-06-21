import random


class Puzzle:
    ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    PUZZLES = ['Kiss and Tell', 'Forgiveness and Stuff', 'Concert Interruptus', 'That Damn Donna Reed',
               'The Third Lorelai', 'Love, Daisies, and Troubadours']

    def __init__(self):
        self.puzzle = ""
        self.hashed_puzzle = ""
        self.alpha_to_hash = dict()
        self.alpha_to_guesses = {
            Puzzle.ALPHABET[i]: '_' for i in range(len(Puzzle.ALPHABET))}

    def reset_puzzle(self):
        self.puzzle = ""
        self.hashed_puzzle = ""
        self.alpha_to_hash = dict()
        self.alpha_to_guesses = {
            Puzzle.ALPHABET[i]: '_' for i in range(len(Puzzle.ALPHABET))}

    def select_puzzle(self):
        self.puzzle = random.choice(Puzzle.PUZZLES)

    def hash_puzzle(self):
        alphabet = list.copy(Puzzle.ALPHABET)
        random.shuffle(alphabet)
        self.alpha_to_hash = {
            Puzzle.ALPHABET[i]: alphabet[i] for i in range(len(Puzzle.ALPHABET))}

        for letter in self.puzzle:
            if not letter.isalpha():
                self.hashed_puzzle += letter
            elif letter.upper() in Puzzle.ALPHABET:
                self.hashed_puzzle += self.alpha_to_hash[letter.upper()]

        self.hashed_puzzle = "  ".join(self.hashed_puzzle.split())

    def update_puzzle_with_guess(self, alpha, guess):
        self.alpha_to_guesses[alpha.upper()] = guess.upper()

    def display_puzzle(self):
        print(self.puzzle)
        print(self.alpha_to_hash)
        print(self.hashed_puzzle)
        print(self.alpha_to_guesses)


if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.select_puzzle()
    puzzle.hash_puzzle()
    puzzle.display_puzzle()
    puzzle.update_puzzle_with_guess('A', 'B')
    puzzle.display_puzzle()
