from common.utils import read_file
import unittest
from .secret import part_one


class TestSecret(unittest.TestCase):
    def setUp(self):
        input = read_file("d25/data/sample1.txt", int)
        self.card = input[0]
        self.door = input[1]

    def test_part_one(self):
        expected = 14897079
        result = part_one(self.card, self.door)
        self.assertEqual(expected, result)

    def test_part_one_2(self):
        expected = 14897079
        result = part_one(self.door, self.card)
        self.assertEqual(expected, result)
