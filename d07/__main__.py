from common.utils import read_file
from .bags import Factory


def main() -> None:
    rules = Factory.from_rules(read_file("d07/data/input.txt"))

    result = rules.count_outside_colors("shiny gold")
    print(f"Result 1: {result}")

    result2 = rules.count_inside_bags("shiny gold")
    print(f"Result 2: {result2}")


if __name__ == "__main__":
    main()
