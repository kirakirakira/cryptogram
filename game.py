from puzzle import Puzzle


class Game:

    def __init__(self):
        self.puzzle = Puzzle()
        # self.puzzle.get_key()
        # self.puzzle.get_puzzle()
        # self.puzzle.hash_the_puzzle()
        # self.turns = 0
        self.turns = 0

    def ask_user_to_play(self):
        response = input("Do you want to play? (y/n) ").lower()
        if response == "y":
            print("Let's play!")
            self.puzzle.reset_puzzle()
            self.puzzle.get_key()
            self.puzzle.get_puzzle()
            self.puzzle.hash_the_puzzle()
            self.ask_user_to_set_difficulty()
        else:
            print("See you later!")
        return response

    def ask_user_to_set_difficulty(self):
        difficulty = input(
            "What difficulty would you like to play? (easy (E)/medium (M)/hard (H)) ").upper()
        num_unique_characters = len(set("".join(self.puzzle.puzzle.split())))

        if difficulty == 'EASY' or difficulty == 'E':
            self.turns = num_unique_characters * 5
        elif difficulty == 'MEDIUM' or difficulty == 'M':
            self.turns = num_unique_characters * 3
        else:
            self.turns = num_unique_characters * 1
        print(f'difficulty is {self.turns}')

    def play_round(self):
        self.puzzle.update_puzzle()
        self.puzzle.display_puzzle()

        won = False

        while not won and self.turns > 0:
            letter_to_replace = input(
                "What letter would you like to replace? ").upper()
            letter_to_replace_with = input(
                "What letter would you like to replace it with? ").upper()
            self.puzzle.guess_a_letter(
                letter_to_replace, letter_to_replace_with)
            self.turns -= 1
            print(f'turns left {self.turns}')
            self.puzzle.update_puzzle()
            self.puzzle.display_puzzle()
            won = self.puzzle.puzzle_matches_key()

        if self.turns >= 0:
            print("You won!")
        else:
            print("You lost!")

    def play_game(self):
        play_again = self.ask_user_to_play()
        while play_again != 'n':
            self.play_round()
            play_again = self.ask_user_to_play()


if __name__ == '__main__':
    game = Game()
    game.play_game()
