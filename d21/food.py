import re
from typing import Iterable

pattern = re.compile(
    r"^(?P<ingredients>[^\(]+) \(contains (?P<allergens>[^\)]+)\)$")


def parse(line: str) -> "Food":
    match = pattern.match(line)
    if not match:
        raise Exception
    ingredients = match["ingredients"].strip().split(" ")
    allergens = match["allergens"].strip().split(", ")

    return Food(ingredients, allergens)


def possible_ingredients(food_list: list["Food"]) -> dict[str, set[str]]:
    result = dict[str, set[str]]()
    for food in food_list:
        for allergene in food.allergenes:
            if allergene not in result:
                result[allergene] = food.ingredients.copy()
            else:
                result[allergene].intersection_update(food.ingredients)
    return result


def get_impossible_ingredients(food_list: list["Food"]) -> set[str]:
    all_ingredients = set[str]()
    for food in food_list:
        all_ingredients.update(food.ingredients)

    possible = set[str]()
    for ingredients in possible_ingredients(food_list).values():
        possible.update(ingredients)
    return all_ingredients.difference(possible)


def count_impossible(food_list: list["Food"]) -> int:
    impossible = get_impossible_ingredients(food_list)

    return sum(
        len(impossible.intersection(food.ingredients)) for food in food_list)


def get_allergenes(food_list: list["Food"]) -> dict[str, str]:
    possible = possible_ingredients(food_list)

    # Reduce
    while any(len(ing) > 1 for ing in possible.values()):
        changed = False
        for ing in possible.values():
            if len(ing) == 1:
                for ing2 in possible.values():
                    if ing < ing2:
                        ing2 -= ing
                        changed = True

        if not changed:
            raise Exception("Could not reduce to single oingredient")

    return {a: i.pop() for a, i in possible.items()}


def get_canonical(food_list: list["Food"]) -> str:
    translated = get_allergenes(food_list)
    return ",".join(ingredient for _, ingredient in sorted(translated.items()))


class Food:
    def __init__(self, ingredients: Iterable[str], allergenes: Iterable[str]):
        self.ingredients = set(ingredients)
        self.allergenes = set(allergenes)
