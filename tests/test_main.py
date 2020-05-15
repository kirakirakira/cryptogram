import unittest

import game
from fractions import Fraction


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 4)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()


# to run tests, do `python3 -m unittest -v tests.test_main`