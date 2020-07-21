from unittest import mock
import game
import unittest


class TestGame(unittest.TestCase):

    @mock.patch('game.ask_user_to_set_difficulty', create=True)
    def test_ask_user_to_set_difficulty(self, mocked_input):
        mocked_input.side_effect = 'H'
        self.assertEqual(next(mocked_input.side_effect), 'H')
    


if __name__ == '__main__':
    unittest.main()