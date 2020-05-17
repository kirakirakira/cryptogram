from unittest.mock import patch
import io
import unittest
import re

from game import game

class TestSum(unittest.TestCase):

    def test_input_yes(self):
        user_input = 'y'

        expected = "Let's play!"

        with patch('builtins.input', side_effect=user_input):
            actual = game.get_start()
        self.assertEqual(actual, expected)

    def test_input_no(self):
        user_input = 'n'

        expected = "See you later!"

        with patch('builtins.input', side_effect=user_input):
            actual = game.get_start()
        self.assertEqual(actual, expected)

    def test_get_puzzle(self):
        puzzle = "I am going to play this game"
        expected = "     ".join(puzzle.split())
        expected = re.sub("[a-zA-Z]", "_ ", expected)

        actual = game.get_puzzle()

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()


# to run tests, do `python3 -m unittest -v tests.test_game`