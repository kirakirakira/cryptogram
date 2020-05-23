import re
import random

puzzle = "I am going to play this game"

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
original_alphabet = list.copy(alphabet)
random.shuffle(alphabet)

key = {original_alphabet[i]: alphabet[i]
       for i in range(len(original_alphabet))}

class Game:

    def __init__(self):
        pass

    def ask_user_to_play(self):
        response = input("Do you want to play? (y/n) ").lower()
        if response == "y":
            print("Let's play!")
        else:
            print("See you later!")
        return response

    def get_puzzle(self):
        transformed_puzzle = "     ".join(puzzle.split())
        transformed_puzzle = re.sub("[a-zA-Z]", "_ ", transformed_puzzle)

        print(transformed_puzzle)

    def play_round(self):
        self.get_puzzle()

    def play_game(self):
        play_again = None
        while play_again != 'n':
            self.play_round()
            play_again = self.ask_user_to_play()


if __name__ == '__main__':
    game = Game()
    game.play_game()
