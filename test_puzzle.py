from unittest import mock
import random
import io
import unittest
import re

from puzzle import Puzzle

def blah(values):
    return "Die, Jerk"

class TestPuzzle(unittest.TestCase):
    def setUp(self):
        self.puzzle = Puzzle()

    def test_choose_puzzle(self):
        with mock.patch('random.choice', blah):
            self.puzzle.select_puzzle()
            actual = self.puzzle.puzzle
            self.puzzle.display_puzzle()

        self.assertEqual(actual, "Die, Jerk")


if __name__ == '__main__':
    unittest.main()
