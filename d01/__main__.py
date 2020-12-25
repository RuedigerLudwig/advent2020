from math import prod
from typing import Optional
from common.utils import read_file
from .calculator import find


def output(result: Optional[list[int]]) -> None:
    if result is None:
        print("No result found")
    else:
        print(f"Result: {result} multiplies to {prod(result)}")


def main() -> None:
    numbers = read_file('d01/data/input.txt', int)
    for i in range(1, 5):
        output(find(numbers, 2020, i))


if __name__ == "__main__":
    main()
