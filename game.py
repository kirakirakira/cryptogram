from puzzle import Puzzle


class Game:

    def __init__(self):
        self.puzzle = Puzzle()
        self.puzzle.get_key()
        self.puzzle.get_puzzle()
        self.puzzle.hash_the_puzzle()

    def ask_user_to_play(self):
        response = input("Do you want to play? (y/n) ").lower()
        if response == "y":
            print("Let's play!")
        else:
            print("See you later!")
        return response

    def play_round(self):
        self.puzzle.update_puzzle()
        self.puzzle.display_puzzle()

        won = False

        while not won:
            letter_to_replace = input(
                "What letter would you like to replace? ").upper()
            letter_to_replace_with = input(
                "What letter would you like to replace it with? ").upper()
            self.puzzle.guess_a_letter(
                letter_to_replace, letter_to_replace_with)
            self.puzzle.update_puzzle()
            self.puzzle.display_puzzle()
            won = self.puzzle.puzzle_matches_key()
        
        print("You won!")

    def play_game(self):
        play_again = self.ask_user_to_play()
        while play_again != 'n':
            self.play_round()
            play_again = self.ask_user_to_play()


if __name__ == '__main__':
    game = Game()
    game.play_game()
