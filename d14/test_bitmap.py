import unittest
from common.utils import read_file
from . import bitmap


class TestBitmap(unittest.TestCase):
    def test_mask8(self):
        mask = bitmap.get_mask("mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        value = 11
        expected = 73
        result = bitmap.apply_mask(mask, value)
        self.assertEqual(expected, result)

    def test_mask7(self):
        mask = bitmap.get_mask("mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        value = 101
        expected = 101
        result = bitmap.apply_mask(mask, value)
        self.assertEqual(expected, result)

    def test_version1(self):
        expected = 165
        lines = read_file("d14/data/sample1.txt")
        result = bitmap.run_version_1(lines)
        self.assertEqual(expected, result)

    def test_floating_mask42(self):
        mask = bitmap.get_mask("mask = 000000000000000000000000000000X1001X")
        value = 42
        expected = {26, 27, 58, 59}
        result = set(bitmap.apply_floating_mask(mask, value))
        self.assertEqual(expected, result)

    def test_floating_mask26(self):
        mask = bitmap.get_mask("mask = 00000000000000000000000000000000X0XX")
        value = 26
        expected = {16, 17, 18, 19, 24, 25, 26, 27}
        result = set(bitmap.apply_floating_mask(mask, value))
        self.assertEqual(expected, result)

    def test_version2(self):
        expected = 208
        lines = read_file("d14/data/sample2.txt")
        result = bitmap.run_version_2(lines)
        self.assertEqual(expected, result)
