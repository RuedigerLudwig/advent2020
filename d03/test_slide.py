from common.utils import read_file
from .forrest import Factory
import unittest


class SlideTest(unittest.TestCase):
    def setUp(self):
        trees = read_file("d03/data/sample1.txt")
        self.forrest = Factory.from_matrix(trees)

    def test_forrest(self):
        expected_width = 11
        expected_hight = 11

        self.assertEqual(expected_width, self.forrest.width)
        self.assertEqual(expected_hight, self.forrest.hight)

    def test_trees(self):
        expected = 7

        result = self.forrest.slope(3, 1).count_trees()

        self.assertEqual(expected, result)
