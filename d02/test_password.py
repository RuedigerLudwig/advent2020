import unittest
from common.utils import read_file
from .password import Factory


class PasswordTest(unittest.TestCase):
    def setUp(self):
        self.passwords = read_file("d02/data/sample1.txt", Factory.fromString)

    def test_version_sled(self):
        expected = ["abcde", "ccccccccc"]

        result = [
            p.password for p in self.passwords
            if p is not None and p.is_valid_sled()
        ]

        self.assertEqual(expected, result)

    def test_version_toboggan(self):
        expected = ["abcde"]

        result = [
            p.password for p in self.passwords
            if p is not None and p.is_valid_tobbogan()
        ]

        self.assertEqual(expected, result)
