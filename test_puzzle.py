from unittest import mock
import random
import io
import unittest
import re

from puzzle import Puzzle


ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def puzzle(values):
    return "Die, Jerk"


def alphabet(values, length):
    return ['B', 'O', 'D', 'V', 'W', 'E', 'U', 'A',
            'L', 'M', 'T', 'R', 'K', 'I', 'G', 'S', 'N',
            'Y', 'Z', 'P', 'C', 'Q', 'X', 'F', 'J', 'H']


class TestPuzzle(unittest.TestCase):
    def setUp(self):
        self.puzzle = Puzzle()

        with mock.patch('random.choice', puzzle):
            self.puzzle.select_puzzle()
            with mock.patch('random.sample', alphabet):
                self.puzzle.hash_puzzle()

    def test_select_puzzle(self):
        actual = self.puzzle.puzzle
        self.assertEqual(actual, "Die, Jerk")

    def test_hash_puzzle(self):
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
        alpha = 'V'
        guess = 'D'
        self.puzzle.update_guesses(alpha, guess)
        self.puzzle.update_guessed_puzzle()

        actual = self.puzzle.guessed_puzzle
        expected = "D__,  ____"
        self.assertEqual(actual, expected)

    def test_lose(self):
        actual = self.puzzle.hashed_puzzle
        expected = False
        actual = self.puzzle.puzzle_matches_key()
        self.assertEqual(actual, expected)

    def test_win(self):
        actual = self.puzzle.hashed_puzzle
        alpha_to_guesses = {'V': 'D', 'L': 'I',
                            'W': 'E', 'M': 'J', 'Y': 'R', 'T': 'K'}

        for alpha, guess in alpha_to_guesses.items():
            self.puzzle.update_guesses(alpha, guess)

        expected = True
        actual = self.puzzle.puzzle_matches_key()
        self.assertEqual(actual, expected)

    def test_reset_puzzle(self):
        self.puzzle.reset_puzzle()

        actual_puzzle = self.puzzle.puzzle
        expected_puzzle = ""
        self.assertEqual(actual_puzzle, expected_puzzle)

        actual_hashed_puzzle = self.puzzle.hashed_puzzle
        expected_hashed_puzzle = ""
        self.assertEqual(actual_hashed_puzzle, expected_hashed_puzzle)

        actual_guessed_puzzle = self.puzzle.guessed_puzzle
        expected_guessed_puzzle = ""
        self.assertEqual(actual_guessed_puzzle, expected_guessed_puzzle)

        actual_alpha_to_hash = self.puzzle.alpha_to_hash
        expected_alpha_to_hash = dict()
        self.assertEqual(actual_alpha_to_hash, expected_alpha_to_hash)

        actual_hash_to_alpha = self.puzzle.hash_to_alpha
        expected_hash_to_alpha = dict()
        self.assertEqual(actual_hash_to_alpha, expected_hash_to_alpha)

        actual_alpha_to_guesses = self.puzzle.alpha_to_guesses
        expected_alpha_to_guesses = {
            ALPHABET[i]: '_' for i in range(len(ALPHABET))}
        self.assertEqual(actual_alpha_to_guesses, expected_alpha_to_guesses)


if __name__ == '__main__':
    unittest.main()
