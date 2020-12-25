import unittest
from . import puzzle


class TestPuzzle(unittest.TestCase):
    def test_version_1_1(self):
        expected = 436
        start = [0, 3, 6]
        result = puzzle.play_game(start, 2020)
        self.assertEqual(expected, result)

    def test_version_1_2(self):
        expected = 1
        start = [1, 3, 2]
        result = puzzle.play_game(start, 2020)
        self.assertEqual(expected, result)

    def _test_version_2_1(self):
        expected = 175594
        start = [0, 3, 6]
        result = puzzle.play_game(start, 30000000)
        self.assertEqual(expected, result)

    def _test_version_2_2(self):
        expected = 2578
        start = [1, 3, 2]
        result = puzzle.play_game(start, 30000000)
        self.assertEqual(expected, result)
