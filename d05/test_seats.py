import unittest
from .seat import Factory


class TestSeat(unittest.TestCase):
    def test_seat1(self):
        expected = 357
        input = "FBFBBFFRLR"
        result = Factory.from_string(input)

        self.assertEqual(expected, result)

    def test_seat2(self):
        expected = 567
        input = "BFFFBBFRRR"
        result = Factory.from_string(input)

        self.assertEqual(expected, result)

    def test_seat3(self):
        expected = 119
        input = "FFFBBBFRRR"
        result = Factory.from_string(input)

        self.assertEqual(expected, result)

    def test_seat4(self):
        expected = 820
        input = "BBFFBBFRLL"
        result = Factory.from_string(input)

        self.assertEqual(expected, result)
