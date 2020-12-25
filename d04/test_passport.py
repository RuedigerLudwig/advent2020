import unittest
from common.utils import count, read_file
from .passport import Factory
from .validator import PassportValidator


class PassportTest(unittest.TestCase):
    def test_stage_1(self):
        pattern = read_file("d04/data/sample1.txt")

        expected = 2
        passports = Factory.from_string(pattern)

        result = count(passports, PassportValidator.is_valid)

        self.assertEqual(expected, result)

    def test_invalid(self):
        pattern = read_file("d04/data/invalids.txt")

        expected = 0
        passports = Factory.from_string(pattern)

        result = count(passports, PassportValidator.is_strictly_valid)

        self.assertEqual(expected, result)

    def test_valid(self):
        pattern = read_file("d04/data/valids.txt")
        expected = 4
        passports = Factory.from_string(pattern)

        result = count(passports, PassportValidator.is_strictly_valid)

        self.assertEqual(expected, result)
