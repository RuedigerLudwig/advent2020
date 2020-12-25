import unittest
from common.interesting import combinations


class TestPermutations(unittest.TestCase):
    input = [1, 2, 3, 4]

    def test_permutations0a(self):
        input = []
        expected = []
        result = list(combinations(input, 2))
        self.assertEqual(expected, result)

    def test_permutations0b(self):
        expected = []
        result = list(combinations(TestPermutations.input, 0))
        self.assertEqual(expected, result)

    def test_permutations1(self):
        expected = [(1, ), (2, ), (3, ), (4, )]
        result = list(combinations(TestPermutations.input, 1))
        self.assertEqual(expected, result)

    def test_permutations2(self):
        expected = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        result = list(combinations(TestPermutations.input, 2))
        self.assertEqual(expected, result)

    def test_permutations3(self):
        expected = [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
        result = list(combinations(TestPermutations.input, 3))
        self.assertEqual(expected, result)

    def test_permutations4(self):
        expected = [(1, 2, 3, 4)]
        result = list(combinations(TestPermutations.input, 4))
        self.assertEqual(expected, result)

    def test_permutations5(self):
        expected = []
        result = list(combinations(TestPermutations.input, 5))
        self.assertEqual(expected, result)
