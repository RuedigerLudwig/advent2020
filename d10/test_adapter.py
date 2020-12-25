import unittest
from common.utils import read_file, safe_int
from .adapters import get_differences, get_num_arrangements


class AdapterTest1(unittest.TestCase):
    def setUp(self):
        self.adapters = read_file('d10/data/sample1.txt', safe_int)

    def test_example_1(self):
        expected = 35
        result = get_differences(self.adapters)

        self.assertEqual(expected, result)

    def test_example_12(self):
        expected = 8
        result = get_num_arrangements(self.adapters)

        self.assertEqual(expected, result)


class AdapterTest2(unittest.TestCase):
    def setUp(self):
        self.adapters = read_file('d10/data/sample2.txt', safe_int)

    def test_example_2(self):
        expected = 220
        result = get_differences(self.adapters)

        self.assertEqual(expected, result)

    def test_example_22(self):
        expected = 19208
        result = get_num_arrangements(self.adapters)

        self.assertEqual(expected, result)


class AdapterTest3(unittest.TestCase):
    def test_example_32(self):
        adapters = read_file('d10/data/sample3.txt', safe_int)
        expected = 7
        result = get_num_arrangements(adapters)

        self.assertEqual(expected, result)
