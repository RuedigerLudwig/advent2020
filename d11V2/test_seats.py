import unittest
from common.utils import read_file
from .room import RoomFactory


class TestSeats(unittest.TestCase):
    def test_find_next(self):
        seats = RoomFactory.version_one(read_file('d11/data/initial.txt'))
        expected = RoomFactory.version_one(read_file('d11/data/round1.txt'))
        result = seats.simulate(4)

        self.assertEqual(expected, result)

    def test_find_second(self):
        seats = RoomFactory.version_one(read_file('d11/data/round1.txt'))
        expected = RoomFactory.version_one(read_file('d11/data/round2.txt'))
        result = seats.simulate(4)

        self.assertEqual(expected, result)

    def test_find_fixed(self):
        seats = RoomFactory.version_one(read_file('d11/data/initial.txt'))
        expected = RoomFactory.version_one(read_file('d11/data/stable.txt'))
        result = seats.find_static(4)
        self.assertEqual(expected, result)
        self.assertEqual(37, result.count_occupied())

    def test_find_second2(self):
        seats = RoomFactory.version_two(read_file('d11/data/round1.txt'))
        expected = RoomFactory.version_two(read_file('d11/data/round2b.txt'))
        result = seats.simulate(5)

        self.assertEqual(expected, result)

    def test_find_fixed2(self):
        seats = RoomFactory.version_two(read_file('d11/data/initial.txt'))
        expected = RoomFactory.version_two(read_file('d11/data/stable_b.txt'))
        result = seats.find_static(5)
        self.assertEqual(expected, result)
        self.assertEqual(26, result.count_occupied())
