import math
from common.utils import read_file
from .row import Row
from .parser import parse


def main() -> None:
    lines = read_file("d20/data/input.txt")
    picture = parse(lines)

    # Part1
    result1 = math.prod(t.number for t in picture.get_corners())
    print(f"Result 1-> {result1} <-1")

    # Part2
    monster = read_file("d20/data/monster.txt", Row.from_string)
    _, result2, _ = picture.apply_monster(monster)
    # result2 = 0
    print(f"Result 2-> {result2} <-2")


if __name__ == "__main__":
    main()
