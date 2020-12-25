from common.timer import Timer
from . import puzzle


@Timer()
def main() -> None:
    starting_numbers = [12, 20, 0, 6, 1, 17, 7]

    result = puzzle.play_game(starting_numbers, 2020)
    print(f"The       2020th number spoken is: {result}")

    result2 = puzzle.play_game(starting_numbers, 30000000)
    print(f"The 30.000.000th number spoken is: {result2}")


if __name__ == "__main__":
    main()
