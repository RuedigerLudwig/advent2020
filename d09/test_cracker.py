from common.utils import read_file
import unittest
from .cracker import get_incorrect_pos, get_weakness


class TestCracker(unittest.TestCase):
    def setUp(self):
        self.numbers = read_file('d09/data/sample1.txt', int)

    def test_crack(self):
        expected = 14
        result = get_incorrect_pos(self.numbers, 5)

        self.assertEqual(expected, result)

    def test_weakness(self):
        expected = [15, 25, 47, 40]
        result = get_weakness(self.numbers, 14)

        self.assertEqual(expected, result)
