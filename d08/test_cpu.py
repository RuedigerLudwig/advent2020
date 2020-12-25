from common.utils import read_file
import unittest
from .cpu import Factory


class TestCpu(unittest.TestCase):
    def setUp(self):
        self.code = Factory.get_code(read_file("d08/data/sample1.txt"))

    def test_parse(self):
        expected = [("nop", 0), ("acc", 1), ("jmp", 4), ("acc", 3),
                    ("jmp", -3), ("acc", -99), ("acc", +1), ("jmp", -4),
                    ("acc", 6)]
        self.assertListEqual(expected, self.code.code)

    def test_loop(self):
        expected = 5, False
        result = self.code.run()
        self.assertEqual(expected, result)

    def test_repaired(self):
        expected = 8
        result = self.code.run_fixed()
        self.assertEqual(expected, result)
