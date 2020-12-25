from common.utils import read_file
from math import prod
from .forrest import Factory


def main() -> None:
    trees = read_file("d03/data/input.txt")

    forrest = Factory.from_matrix(trees)
    slope = forrest.slope(3, 1)

    print(f"Result 1: Encountered {slope.count_trees()} trees")

    to_be_checked = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = prod(
        forrest.slope(right, down).count_trees()
        for right, down in to_be_checked)
    print(f"Result 2: The tree product is {result}")


if __name__ == "__main__":
    main()
