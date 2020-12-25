from common.utils import read_file
from . import food


def main() -> None:
    food_list = read_file("d21/data/input.txt", food.parse)

    # Part1
    result1 = food.count_impossible(food_list)
    print(f"Result 1-> {result1} <-1")

    # Part2
    result2 = food.get_canonical(food_list)
    print(f"Result 2-> {result2} <-2")


if __name__ == "__main__":
    main()
