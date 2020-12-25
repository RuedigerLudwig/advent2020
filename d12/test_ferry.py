import unittest
from common.utils import read_file
from .storm import StormFactory


class TestFerry(unittest.TestCase):
    def test_distance(self):
        expected = 25
        actions = read_file("d12/data/sample1.txt", StormFactory.from_string)
        result = StormFactory.get_distance(actions)

        self.assertEqual(expected, result)

    def test_waypoint_distance(self):
        expected = 286
        actions = read_file("d12/data/sample1.txt", StormFactory.from_string)
        result = StormFactory.get_waypoint_distance(actions)

        self.assertEqual(expected, result)
