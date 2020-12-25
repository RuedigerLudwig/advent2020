from common.utils import read_file
from .bitmap import run_version_1, run_version_2


def main() -> None:
    lines = read_file("d14/data/input.txt")
    result = run_version_1(lines)
    print(f"The value is {result}")

    result2 = run_version_2(lines)
    print(f"The real value is {result2}")


if __name__ == "__main__":
    main()
