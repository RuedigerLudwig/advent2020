from common.utils import read_file
from .seat import Factory


def main() -> None:
    seats = read_file("d05/data/input.txt", Factory.from_string)

    result = max(seats)
    print(f"Result 1: The maximum number is {result}")

    seat = Factory.find_missing(seats)
    print(f"Result 2: Your seat is {seat}")


if __name__ == "__main__":
    main()
