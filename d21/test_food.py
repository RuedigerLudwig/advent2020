import unittest
from common.utils import read_file
from . import food


class TestFood(unittest.TestCase):
    def test_parse_ingredients(self):
        input = "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)"
        expected = set(["mxmxvkd", "kfcds", "sqjhc", "nhms"])
        result = food.parse(input)
        self.assertSetEqual(expected, result.ingredients)

    def test_parse_allergens(self):
        input = "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)"
        expected = set(["dairy", "fish"])
        result = food.parse(input)
        self.assertSetEqual(expected, result.allergenes)

    def test_possible_fish(self):
        expected = set[str](["mxmxvkd", "sqjhc"])
        food_list = read_file("d21/data/sample1.txt", food.parse)
        result = food.possible_ingredients(food_list)
        self.assertSetEqual(expected, result["fish"])

    def test_impossible(self):
        expected = set[str](["kfcds", "nhms", "sbzzf", "trh"])
        food_list = read_file("d21/data/sample1.txt", food.parse)
        result = food.get_impossible_ingredients(food_list)
        self.assertSetEqual(expected, result)

    def test_count_impossible(self):
        expected = 5
        food_list = read_file("d21/data/sample1.txt", food.parse)
        result = food.count_impossible(food_list)
        self.assertEqual(expected, result)

    def test_get_found(self):
        expected = "sqjhc"
        food_list = read_file("d21/data/sample1.txt", food.parse)
        result = food.get_allergenes(food_list)
        self.assertEqual(expected, result["fish"])

    def test_canonical(self):
        expected = "mxmxvkd,sqjhc,fvjkl"
        food_list = read_file("d21/data/sample1.txt", food.parse)
        result = food.get_canonical(food_list)
        self.assertEqual(expected, result)
