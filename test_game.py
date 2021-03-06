from unittest import mock
import game
from game import Game
import unittest


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    @mock.patch('builtins.input', return_value = 'H')
    def test_ask_user_to_set_difficulty(self, mocked_input):
        result = self.game.ask_user_to_set_difficulty()
        self.assertEqual(result, 'H')

    @mock.patch('builtins.input', return_value = 'y')
    def test_ask_user_to_play(self, mocked_input):
        result = self.game.ask_user_to_play()
        self.assertEqual(result, 'y')


if __name__ == '__main__':
    unittest.main()