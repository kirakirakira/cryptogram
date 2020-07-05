from unittest import mock
import random
import io
import unittest
import re

from puzzle import Puzzle


def puzzle(values):
    return "Die, Jerk"


def alphabet(values, length):
    return ['B', 'O', 'D', 'V', 'W', 'E', 'U', 'A',
            'L', 'M', 'T', 'R', 'K', 'I', 'G', 'S', 'N',
            'Y', 'Z', 'P', 'C', 'Q', 'X', 'F', 'J', 'H']

def hashed_puzzle(values):
    return "VLW, MWYT"

def alpha_to_guesses(values):
    return {'A': '', 'B': '', 'C': ''}

def hash_to_alpha(values):
    return {'B': 'A'}


class TestPuzzle(unittest.TestCase):
    def setUp(self):
        self.puzzle = Puzzle()

    def test_select_puzzle(self):
        with mock.patch('random.choice', puzzle):
            self.puzzle.select_puzzle()
            actual = self.puzzle.puzzle

        self.assertEqual(actual, "Die, Jerk")

    def test_hash_puzzle(self):
        with mock.patch('random.choice', puzzle):
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

    def test_update_guessed_puzzle(self):
        with mock.patch('random.choice', puzzle):
            self.puzzle.select_puzzle()
            with mock.patch('random.sample', alphabet):
                self.puzzle.hash_puzzle()
                actual = self.puzzle.hashed_puzzle
                expected = "VLW,  MWYT"
        alpha = 'V'
        guess = 'D'
        self.puzzle.update_guesses(alpha, guess)
        self.puzzle.update_guessed_puzzle()

        actual = self.puzzle.guessed_puzzle
        expected = "D__,  ____"
        
        self.assertEqual(actual, expected)

    def test_lose(self):
        with mock.patch('random.choice', puzzle):
            self.puzzle.select_puzzle()
            with mock.patch('random.sample', alphabet):
                self.puzzle.hash_puzzle()
                actual = self.puzzle.hashed_puzzle

        expected = False
        actual = self.puzzle.puzzle_matches_key()
        self.assertEqual(actual, expected)

    def test_win(self):
        with mock.patch('random.choice', puzzle):
            self.puzzle.select_puzzle()
            with mock.patch('random.sample', alphabet):
                self.puzzle.hash_puzzle()
                actual = self.puzzle.hashed_puzzle

        alpha_to_guesses = {'V': 'D', 'L': 'I', 'W': 'E', 'M': 'J', 'Y': 'R', 'T': 'K'}

        for alpha, guess in alpha_to_guesses.items():
            self.puzzle.update_guesses(alpha, guess)
        
        expected = True
        actual = self.puzzle.puzzle_matches_key()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
