from common.utils import count, read_file
from .passport import Factory
from .validator import PassportValidator


def main() -> None:
    pattern = read_file("d04/data/input.txt")
    passports = list(Factory.from_string(pattern))

    result = count(passports, PassportValidator.is_valid)
    print(f"Result 1 : There are {result} valid passports")

    result = count(passports, PassportValidator.is_strictly_valid)
    print(f"Result 2 : There are {result} strickly valid passports")


if __name__ == "__main__":
    main()
