import unittest
from . import crab


class TestCrab(unittest.TestCase):
    def test_one_1(self):
        input = "389125467"
        expected = "54673289"
        result = crab.play_game(input, 1).string_result(1)
        self.assertEqual(expected, result)

    def test_part_one_10(self):
        input = "389125467"
        expected = "92658374"
        result = crab.play_game(input, 10).string_result(1)
        self.assertSequenceEqual(expected, result)

    def test_part_one_100(self):
        input = "389125467"
        expected = "67384529"
        result = crab.play_game(input, 100).string_result(1)
        self.assertEqual(expected, result)

    def _test_part_2(self):
        input = "389125467"
        expected = 934001, 159792
        result = crab.play_game(input, 10_000_000, 1_000_000).tuple_result(1)
        self.assertTupleEqual(expected, result)
