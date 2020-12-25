from common.utils import read_file
from .secret import part_one


def main() -> None:
    input = read_file("d25/data/input.txt", int)

    # Part1
    result1 = part_one(input[0], input[1])
    print(f"Result 1-> {result1} <-1")


if __name__ == "__main__":
    main()
