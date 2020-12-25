from common.utils import read_file
from .cracker import get_incorrect_pos, get_weakness


def main() -> None:
    numbers = read_file('d09/data/input.txt', int)

    result = get_incorrect_pos(numbers, 25)
    if result:
        print(f"Result 1: {numbers[result]}")

        result2 = get_weakness(numbers, result)
        if result2:
            print(f"Result 2: {min(result2) + max(result2)}")
    else:
        print("No  incorrect number found")


if __name__ == "__main__":
    main()
