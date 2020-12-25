import unittest
from common.utils import read_file
from .bags import Factory


class TestBags(unittest.TestCase):
    def setUp(self):
        self.rules = Factory.from_rules(read_file("d07/data/sample1.txt"))

    def test_parser(self):
        expected = {
            'light red': {
                'bright white': 1,
                'muted yellow': 2,
            },
            'dark orange': {
                'bright white': 3,
                'muted yellow': 4,
            },
            'bright white': {
                'shiny gold': 1,
            },
            'muted yellow': {
                'shiny gold': 2,
                'faded blue': 9,
            },
            'shiny gold': {
                'dark olive': 1,
                'vibrant plum': 2,
            },
            'dark olive': {
                'faded blue': 3,
                'dotted black': 4,
            },
            'vibrant plum': {
                'faded blue': 5,
                'dotted black': 6,
            }
        }
        self.assertDictEqual(expected, self.rules.bags)

    def test_count_outside(self):
        expected = 4
        result = self.rules.count_outside_colors('shiny gold')

        self.assertEqual(expected, result)

    def test_count_inside(self):
        expected = 32
        result = self.rules.count_inside_bags('shiny gold')

        self.assertEqual(expected, result)

    def test_count_inside_2(self):
        rules = Factory.from_rules(read_file("d07/data/sample2.txt"))
        expected = 126
        result = rules.count_inside_bags('shiny gold')

        self.assertEqual(expected, result)
