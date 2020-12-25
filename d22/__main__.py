from common.utils import read_file, Timer
from .factory import GameFactory


def main() -> None:
    lines = read_file("d22/data/input.txt")
    game = GameFactory.parse(lines)

    # Part1
    last_game = game.play_game()
    winner = last_game.winner
    if winner is not None:
        result1 = winner.card_value
        print(f"Result 1-> {result1} <-1")

    # Part2
    advanced = GameFactory.advanced(game)
    with Timer():
        deck, winner = advanced.play_game()
        result2 = GameFactory.value(deck)
        if winner:
            print(f"Result 2-> {result2} <-2 (Player 1)")
        else:
            print(f"Result 2-> {result2} <-2 (Player 2)")


if __name__ == "__main__":
    main()
