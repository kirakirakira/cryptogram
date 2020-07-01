from unittest import mock
import random
import io
import unittest
import re

from puzzle import Puzzle


def blah(values):
    return "Die, Jerk"


def alphabet(values, length):
    return ['B', 'O', 'D', 'V', 'W', 'E', 'U', 'A',
            'L', 'M', 'T', 'R', 'K', 'I', 'G', 'S', 'N',
            'Y', 'Z', 'P', 'C', 'Q', 'X', 'F', 'J', 'H']


class TestPuzzle(unittest.TestCase):
    def setUp(self):
        self.puzzle = Puzzle()

    def test_select_puzzle(self):
        with mock.patch('random.choice', blah):
            self.puzzle.select_puzzle()
            actual = self.puzzle.puzzle

        self.assertEqual(actual, "Die, Jerk")

    def test_hash_puzzle(self):
        with mock.patch('random.choice', blah):
            self.puzzle.select_puzzle()
            with mock.patch('random.sample', alphabet):
                self.puzzle.hash_puzzle()
                actual = self.puzzle.hashed_puzzle
                expected = "VLW,  MWYT"

        self.assertEqual(actual, expected)

    def test_guess_already_used_false(self):
        alpha = 'A'
        guess = 'B'
        actual = self.puzzle.guess_already_used(alpha, guess)
        expected = False

        self.assertEqual(actual, expected)

    def test_guess_already_used_true(self):
        alpha = 'A'
        guess = 'B'
        self.puzzle.update_guesses(alpha, guess)

        actual = self.puzzle.guess_already_used(alpha, guess)
        expected = True

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
