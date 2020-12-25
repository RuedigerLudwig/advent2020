import unittest
from common.utils import read_file
from .tile import Dir, TileFactory


class TestTiles(unittest.TestCase):
    def test_parse(self):
        input = "esenee"
        expected = [Dir.East, Dir.SouthEast, Dir.NorthEast, Dir.East]
        result = list(TileFactory.parse_walk(input))
        self.assertListEqual(expected, result)

    def test_walk_1(self):
        input = "esew"
        expected = (1, -1)
        walk = TileFactory.parse_walk(input)
        result = TileFactory.walk_to_tile(walk)
        self.assertEqual(expected, result)

    def test_walk_2(self):
        input = "nwwswee"
        expected = (0, 0)
        walk = TileFactory.parse_walk(input)
        result = TileFactory.walk_to_tile(walk)
        self.assertEqual(expected, result)


class TestFloor(unittest.TestCase):
    def setUp(self):
        self.floor = TileFactory.parse_lines(read_file("d24/data/sample1.txt"))

    def test_flip_all(self):
        expected = 10
        result = self.floor.count_tiles()
        self.assertEqual(expected, result)

    def test_simulation1(self):
        expected = 15
        floor = self.floor.simulate(1)
        result = floor.count_tiles()
        self.assertEqual(expected, result)

    def test_simulation100(self):
        expected = 2208
        floor = self.floor.simulate(100)
        result = floor.count_tiles()
        self.assertEqual(expected, result)
