import unittest
from .calculator import find


class CalculatorTest(unittest.TestCase):
    data = [1721, 979, 366, 299, 675, 1456]

    def test_version_a(self):
        expected = [1721, 299]
        result = find(CalculatorTest.data, 2020, 2)

        self.assertEqual(expected, result)

    def test_version_a_break(self):
        expected = None
        result = find(CalculatorTest.data, 2021, 2)

        self.assertEqual(expected, result)

    def test_version_b(self):
        expected = [979, 366, 675]
        result = find(CalculatorTest.data, 2020, 3)

        self.assertEqual(expected, result)

    def test_version_b_break(self):
        expected = None
        result = find(CalculatorTest.data, 2021, 3)

        self.assertEqual(expected, result)
