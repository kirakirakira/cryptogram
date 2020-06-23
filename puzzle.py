import random
from soup import Soup


class Puzzle:
    ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    PUZZLES = ['Kiss and Tell', 'Forgiveness and Stuff', 'Concert Interruptus', 'That Damn Donna Reed',
               'The Third Lorelai', 'Love, Daisies, and Troubadours']

    def __init__(self):
        self.puzzle = ""
        self.hashed_puzzle = ""
        self.guessed_puzzle = ""
        self.alpha_to_hash = dict()
        self.alpha_to_guesses = {
            Puzzle.ALPHABET[i]: '_' for i in range(len(Puzzle.ALPHABET))}
        self.soup = Soup()

    def reset_puzzle(self):
        self.puzzle = ""
        self.hashed_puzzle = ""
        self.guessed_puzzle = ""
        self.alpha_to_hash = dict()
        self.alpha_to_guesses = {
            Puzzle.ALPHABET[i]: '_' for i in range(len(Puzzle.ALPHABET))}

    def select_puzzle(self):
        self.puzzle = random.choice(self.soup.get_episodes())

    def hash_puzzle(self):
        alphabet = list.copy(Puzzle.ALPHABET)
        random.shuffle(alphabet)
        self.alpha_to_hash = {
            Puzzle.ALPHABET[i]: alphabet[i] for i in range(len(Puzzle.ALPHABET))}
        self.hash_to_alpha = {
            alphabet[i]: Puzzle.ALPHABET[i]
            for i in range(len(Puzzle.ALPHABET))}

        for letter in self.puzzle:
            if not letter.isalpha():
                self.hashed_puzzle += letter
            elif letter.upper() in Puzzle.ALPHABET:
                self.hashed_puzzle += self.alpha_to_hash[letter.upper()]

        self.hashed_puzzle = "  ".join(self.hashed_puzzle.split())

    def update_guesses(self, alpha, guess):
        if guess in self.alpha_to_guesses.values():
            return True
        else:
            self.alpha_to_guesses[alpha.upper()] = guess.upper()
            return False

    def update_guessed_puzzle(self):
        self.guessed_puzzle = ""
        for letter in self.hashed_puzzle:
            if not letter.isalpha():
                self.guessed_puzzle += letter
            elif letter.upper() in Puzzle.ALPHABET:
                self.guessed_puzzle += self.alpha_to_guesses[letter.upper()]

        self.guessed_puzzle = "  ".join(self.guessed_puzzle.split())

    def puzzle_matches_key(self):
        for letter in self.hashed_puzzle:
            if not letter.isspace() and letter != "\"":
                # don't use letter here, need to look up the alpha letter for each letter that's in the hash
                lookup = self.hash_to_alpha[letter]
                if self.alpha_to_guesses[lookup] == self.alpha_to_hash[lookup]:
                    continue
                else:
                    return False
        return True

    def display_guessed_puzzle(self):
        print(self.guessed_puzzle)

    def display_hashed_puzzle(self):
        print(self.hashed_puzzle)


if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.select_puzzle()
    puzzle.hash_puzzle()
    puzzle.update_guesses('A', 'B')
    puzzle.update_guesses('F', 'E')
    puzzle.update_guesses('T', 'E')
    puzzle.update_guesses('C', 'E')
    puzzle.update_guesses('D', 'E')
    puzzle.update_guesses('L', 'E')
    puzzle.update_guesses('G', 'E')
    puzzle.update_guesses('H', 'E')
    puzzle.update_guesses('I', 'E')
    puzzle.update_guessed_puzzle()
    puzzle.display_guessed_puzzle()
    puzzle.display_hashed_puzzle()
