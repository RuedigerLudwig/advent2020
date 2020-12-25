from common.utils import read_file
from .adapters import get_num_arrangements, get_differences


def main() -> None:
    adapters = read_file('d10/data/input.txt', int)
    result = get_differences(adapters)
    print(f"Result 1: {result}")

    choices = get_num_arrangements(adapters)
    print(f"Result 2: {choices} ")


if __name__ == "__main__":
    main()
