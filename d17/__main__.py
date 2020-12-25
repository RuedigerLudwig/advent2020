from .hyper import Hyper
from common.utils import read_file, Timer


def main() -> None:
    lines = read_file("d17/data/input.txt")

    # Part1
    hyper = Hyper.parse_from_2D(lines, 3)
    with Timer():
        result1 = hyper.run(6).count_active()
        print(f"Result 1-> {result1} <-1")

    # Part2
    hyper = Hyper.parse_from_2D(lines, 4)
    with Timer():
        result2 = hyper.run(6).count_active()
        print(f"Result 2-> {result2} <-2")


if __name__ == "__main__":
    main()
