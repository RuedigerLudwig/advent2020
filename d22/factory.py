from typing import Iterator, Sequence
from .game import Game
from .player import Player
from .recursive import AdvancedGame


class GameFactory:
    @staticmethod
    def parse(lines: list[str]) -> Game:
        def read_player(iter: Iterator[str]) -> Player:
            _ = next(iter)  # Name line

            cards = list[int]()
            try:
                while (num := next(iter)) != "":
                    cards.append(int(num))
            except StopIteration:
                pass
            return Player(tuple(cards))

        it = iter(lines)
        p1 = read_player(it)
        p2 = read_player(it)

        return Game(p1, p2)

    @staticmethod
    def advanced(game: Game) -> AdvancedGame:
        return AdvancedGame(game.p1.cards, game.p2.cards)

    @staticmethod
    def value(deck: Sequence[int]) -> int:
        length = len(deck)
        return sum((length - pos) * v for pos, v in enumerate(deck))
