from unittest import mock
from game import Game
import unittest


def get_input(text):
    return input(text)

def answer():
    ans = get_input("What difficulty would you like to play? (easy (E)/medium (M)/hard (H)) ").upper()
    return ans


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_ask_user_to_set_difficulty(self):
        @mock.patch('Game.ask_user_to_set_difficulty', return_value = 'H')
        def test_answer(self, input):
            self.assertEqual(answer(), 'H')


if __name__ == '__main__':
    unittest.main()