from common.utils import read_file
from .cpu import Factory


def main() -> None:
    code = Factory.get_code(read_file("d08/data/input.txt"))

    acc, _ = code.run()
    print(f"Result 1: {acc}")

    result2 = code.run_fixed()
    print(f"Result 2: {result2}")


if __name__ == "__main__":
    main()
