from common.utils import read_file, Timer
from . import monster


def main() -> None:
    lines = read_file("d19/data/input.txt")

    # Part1
    rules, words = monster.parse_lines(lines)
    result1 = monster.count_matches(words, rules)
    print(f"Result 1-> {result1} <-1")

    # Part2
    rules = monster.mingle_rules(rules)
    with Timer():
        result2 = monster.count_matches(words, rules)
    print(f"Result 2-> {result2} <-2")


if __name__ == "__main__":
    main()
