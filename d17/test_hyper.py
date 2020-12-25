import unittest
from common.utils import read_file
from .hyper import Hyper


class TestHyper3D(unittest.TestCase):
    def setUp(self):
        lines = read_file("d17/data/sample1.txt")
        self.space = Hyper.parse_from_2D(lines, 3)

    def test_initialize(self):
        expected = read_file("d17/data/expected0.txt")
        result = self.space.print()
        self.assertEqual(expected, result)

    def test_run_one(self):
        expected = read_file("d17/data/expected1.txt")
        result = self.space.run(1).print()
        self.assertEqual(expected, result)

    def test_run_two(self):
        expected = read_file("d17/data/expected2.txt")
        result = self.space.run(2).print()
        self.assertEqual(expected, result)

    def _test_run_six(self):
        expected = 112
        result = self.space.run(6).count_active()
        self.assertEqual(expected, result)


class TestHyper4D(unittest.TestCase):
    def setUp(self):
        lines = read_file("d17/data/sample1.txt")
        self.space = Hyper.parse_from_2D(lines, 4)

    def _test_run_six(self):
        expected = 848
        result = self.space.run(6).count_active()
        self.assertEqual(expected, result)

    def test_run_once(self):
        expected = read_file("d17/data/expected21.txt")
        result = self.space.run(1).print()
        self.assertEqual(expected, result)

    def test_run_twice(self):
        expected = read_file("d17/data/expected22.txt")
        result = self.space.run(2).print()
        self.assertEqual(expected, result)
