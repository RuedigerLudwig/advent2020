from common.utils import read_file
from .tokenizer import Tokenizer


def main() -> None:
    lines = read_file("d18/data/input.txt")

    # Part1
    tokens1 = [Tokenizer.simple(line) for line in lines]
    result1 = Tokenizer.sum(tokens1)
    print(f"Result 1-> {result1} <-1")

    # Part2
    tokens2 = [Tokenizer.advanced(line) for line in lines]
    result2 = Tokenizer.sum(tokens2)
    print(f"Result 2-> {result2} <-2")


if __name__ == "__main__":
    main()
