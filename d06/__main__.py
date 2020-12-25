from common.utils import read_file
from .answers import AnswerEval


def main() -> None:
    all_answers = read_file("d06/data/input.txt")

    answers = AnswerEval.by_anyone(all_answers)
    result = sum(len(a) for a in answers)
    print(f"Result 1: There were {result} answers given by anyone")

    answers = AnswerEval.by_everyone(all_answers)
    result = sum(len(a) for a in answers)
    print(f"Result 2: There were {result} answers given by everyone")


if __name__ == "__main__":
    main()
