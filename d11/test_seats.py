import unittest
from common.utils import read_file
from .room import Factory


class TestSeats(unittest.TestCase):
    def test_find_next(self):
        seats = Factory.from_lines(read_file("d11/data/initial.txt"))
        expected = Factory.from_lines(read_file("d11/data/round1.txt"))
        result = seats.simulate()

        self.assertEqual(expected, result)

    def test_find_second(self):
        seats = Factory.from_lines(read_file("d11/data/round1.txt"))
        expected = Factory.from_lines(read_file("d11/data/round2.txt"))
        result = seats.simulate()
        self.assertEqual(expected, result)

    def test_find_fixed(self):
        seats = Factory.from_lines(read_file("d11/data/initial.txt"))
        expected = Factory.from_lines(read_file("d11/data/stable.txt"))
        result = seats.simulate_to_fixed()
        self.assertEqual(expected, result)
        self.assertEqual(37, result.count_seats())

    def test_other_neighbors(self):
        seats = Factory.from_lines(read_file("d11/data/neighbor1.txt"))
        expected = 8
        result = seats.count_other_neighbours(4, 3)
        self.assertEqual(expected, result)

    def test_find_second2(self):
        seats = Factory.from_lines(read_file("d11/data/round1.txt"))
        expected = Factory.from_lines(read_file("d11/data/round2b.txt"))
        result = seats.simulate2()
        self.assertEqual(expected, result)

    def test_find_fixed2(self):
        seats = Factory.from_lines(read_file("d11/data/initial.txt"))
        # seats = Factory.from_lines(read_file("d11/data/input.txt"))
        expected = Factory.from_lines(read_file("d11/data/stable_b.txt"))
        result = seats.simulate_to_fixed2()
        self.assertEqual(expected, result)
        self.assertEqual(26, result.count_seats())
