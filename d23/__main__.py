from common.timer import Timer
from .crab import CrabGame
import math


def main() -> None:
    input = "952438716"
    game = CrabGame.from_string(input)

    # Part1
    result1 = game.run(100).string_result(1)
    print(f"Result 1-> {result1} <-1")

    # Part2
    with Timer():
        result2 = game.pump_up_to(1_000_000).run(10_000_000).tuple_result(1)
        print(f"Result 2-> {math.prod(result2)} <-2")


if __name__ == "__main__":
    main()
