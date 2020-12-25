import unittest
from common.utils import read_file
from .directions import Direction
from .row import Row
from .parser import parse
from .tile import Tile


class TestTiles(unittest.TestCase):
    def setUp(self):
        lines = read_file("d20/data/sample1.txt")
        self.picture = parse(lines)
        pass

    def test_parse(self):
        expected = [
            "Tile 1951:",
            "#.##...##.",
            "#.####...#",
            ".....#..##",
            "#...######",
            ".##.#....#",
            ".###.#####",
            "###.##.##.",
            ".###....#.",
            "..#.#..#.#",
            "#...##.#..",
        ]
        result = self.picture[1951]
        self.assertListEqual(expected, result.as_list())

    def test_count_edges(self):
        expected = (6, 5, 5, 4)
        tile = self.picture[1951]
        result = tuple(edge.dot_count for edge in tile.edges.values())
        self.assertEqual(expected, result)

    def test_get_corners(self):
        expected = {1951, 3079, 2971, 1171}
        result = set(t.number for t in self.picture.get_corners())

        self.assertSetEqual(expected, result)

    def test_get_ordered(self):
        expected = [[3079, 2473, 1171], [2311, 1427, 1489], [1951, 2729, 2971]]
        ordered = self.picture.get_ordered()
        result = [[t.number for t in row] for row in ordered]
        self.assertListEqual(expected, result)

    def test_fit_tile1(self):
        orig = self.picture[1951]
        fixed = orig.rotate_tile(2, True)

        expected = [
            "Tile 2311:",
            "..###..###",
            "###...#.#.",
            "..#....#..",
            ".#.#.#..##",
            "##...#.###",
            "##.##.###.",
            "####.#...#",
            "#...##..#.",
            "##..#.....",
            "..##.#..#.",
        ]
        add = self.picture[2311]
        result = fixed.fit_tile(add, Direction.EAST)
        if result is not None:
            self.assertListEqual(expected, result.as_list())
        self.assertIsNotNone(result)

    def test_fit_tile2(self):
        expected = [
            "Tile 2473:",
            "..#.###...",
            "##.##....#",
            "..#.###..#",
            "###.#..###",
            ".######.##",
            "#.#.#.#...",
            "#.###.###.",
            "#.###.##..",
            ".######...",
            ".##...####",
        ]
        orig = self.picture[3079]
        add = self.picture[2473]
        result = orig.fit_tile(add, Direction.SOUTH)
        if result is not None:
            self.assertListEqual(expected, result.as_list())
        self.assertIsNotNone(result)

    def test_turn_left(self):
        matrix = [
            Row([True, True, False]),
            Row([True, False, False]),
            Row([False, True, False])
        ]
        expected = [
            Row([False, False, False]),
            Row([True, False, True]),
            Row([True, True, False])
        ]
        tile = Tile(1, matrix)
        result = tile.rotate_tile(1, False)
        self.assertListEqual(expected, result.rows)

    def test_turn_right(self):
        matrix = [
            Row([True, True, False]),
            Row([True, False, False]),
            Row([False, True, False])
        ]
        expected = [
            Row([False, True, True]),
            Row([True, False, True]),
            Row([False, False, False])
        ]
        tile = Tile(1, matrix)
        result = tile.rotate_tile(3, False)
        self.assertListEqual(expected, result.rows)

    def test_turn_half(self):
        matrix = [
            Row([True, True, False]),
            Row([True, False, False]),
            Row([False, True, False])
        ]
        expected = [
            Row([False, True, False]),
            Row([False, False, True]),
            Row([False, True, True])
        ]
        tile = Tile(1, matrix)
        result = tile.rotate_tile(2, False)
        self.assertListEqual(expected, result.rows)

    def test_remove_monster(self):
        monster = read_file("d20/data/monster.txt", Row.from_string)
        expected = 273
        _, result, _ = self.picture.apply_monster(monster)
        self.assertEqual(expected, result)
