from common.utils import read_file, Timer
from .tile import TileFactory


def main() -> None:
    floor = TileFactory.parse_lines(read_file("d24/data/input.txt"))

    # Part1
    result1 = floor.count_tiles()
    print(f"Result 1-> {result1} <-1")

    # Part2
    with Timer():
        floor = floor.simulate(100)
    result2 = floor.count_tiles()
    print(f"Result 2-> {result2} <-2")


if __name__ == "__main__":
    main()
