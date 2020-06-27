from puzzle import Puzzle


class Game:
    WON = """\
 __     __                               _
 \ \   / /                              | |
  \ \_/ ___  _   _  __      _____  _ __ | |
   \   / _ \| | | | \ \ /\ / / _ \| '_ \| |
    | | (_) | |_| |  \ V  V | (_) | | | |_|
    |_|\___/ \__,_|   \_/\_/ \___/|_| |_(_)

    """

    LOST = """\
 __     __           _           _   _
 \ \   / /          | |         | | | |
  \ \_/ ___  _   _  | | ___  ___| |_| |
   \   / _ \| | | | | |/ _ \/ __| __| |
    | | (_) | |_| | | | (_) \__ | |_|_|
    |_|\___/ \__,_| |_|\___/|___/\__(_)

    """

    SEEYOULATER = """\
   _____                                 _       _
  / ____|                               | |     | |
 | (___   ___  ___   _   _  ___  _   _  | | __ _| |_ ___ _ __
  \___ \ / _ \/ _ \ | | | |/ _ \| | | | | |/ _` | __/ _ | '__|
  ____) |  __|  __/ | |_| | (_) | |_| | | | (_| | ||  __| |
 |_____/ \___|\___|  \__, |\___/ \__,_| |_|\__,_|\__\___|_|
                      __/ |
                     |___/
    """

    def __init__(self):
        self.puzzle = Puzzle()
        self.turns = 0
        self.won = False

    def ask_user_to_play(self):
        response = input("Do you want to play? (y/n) ").lower()
        if response == "y":
            print("Let's play!")
            self.turns = 0
            self.won = False
            self.puzzle.reset_puzzle()
            self.puzzle.select_puzzle()
            self.puzzle.display_puzzle()
            self.puzzle.hash_puzzle()
            self.ask_user_to_set_difficulty()
        else:
            print(f'{game.SEEYOULATER}')
        return response

    def calculate_difficulty(self, difficulty):
        num_unique_characters = len(set("".join(ch.lower() for ch in self.puzzle.puzzle if ch.isalpha())))

        if difficulty == 'EASY' or difficulty == 'E':
            self.turns = num_unique_characters * 5
        elif difficulty == 'MEDIUM' or difficulty == 'M':
            self.turns = num_unique_characters * 3
        else:
            self.turns = num_unique_characters * 1
        print(f'difficulty is {self.turns}')

    def ask_user_to_set_difficulty(self):
        difficulty = input(
            "What difficulty would you like to play? (easy (E)/medium (M)/hard (H)) ").upper()
        self.calculate_difficulty(difficulty)

    def print_won_or_lost(self, won):
        if self.turns >= 0 and won:
            print(f'{game.WON}')
        else:
            print(f'{game.LOST}')
            print("Answer is: ")
            # display the answer
            print()
            print("*****"*5)
            print()


    def play_round(self):
        while not self.won and self.turns > 0:
            self.puzzle.update_guessed_puzzle()
            self.puzzle.display_guessed_puzzle()
            self.puzzle.display_hashed_puzzle()

            letter_to_replace = input("What letter would you like to replace? ").upper()
            guess = input("What letter would you like to replace it with? ").upper()
            already_used = self.puzzle.update_guesses(letter_to_replace, guess)

            if not already_used:
                self.turns -= 1
            else:
                print()
                print(f'Already used that letter in the puzzle, try again.')

            if self.turns > 0:
                print(f'Turns left {self.turns}')
                print()

            self.won = self.puzzle.puzzle_matches_key()
        
        if self.turns >= 0 and self.won:
            print(f'{game.WON}')
        else:
            print(f'{game.LOST}')
            self.puzzle.display_puzzle()
            self.puzzle.display_hashed_puzzle()
            print()

    def play_game(self):
        play_again = self.ask_user_to_play()
        while play_again != 'n':
            self.play_round()
            play_again = self.ask_user_to_play()


if __name__ == '__main__':
    game = Game()
    game.play_game()
