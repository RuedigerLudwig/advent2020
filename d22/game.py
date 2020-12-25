from .player import Player
from typing import Optional


class Game:
    def __init__(self, p1: Player, p2: Player):
        self._p1 = p1
        self._p2 = p2

    @property
    def winner(self) -> Optional[Player]:
        if self._p1.has_lost():
            return self._p2
        if self._p2.has_lost():
            return self._p1
        return None

    def __str__(self) -> str:
        return f"{self._p1} - {self._p2}"

    def __eq__(self, other: "Game") -> bool:
        return self._p1 == other._p1 and self._p2 == other._p2

    def __hash__(self) -> int:
        return hash(self._p1) ^ hash(self._p2)

    @property
    def p1(self) -> Player:
        return self._p1

    @property
    def p2(self) -> Player:
        return self._p2

    def p1_won(self) -> bool:
        return self.winner == self._p1

    def single_round(self) -> "Game":
        if self.winner is not None:
            return self

        card1 = self._p1.top()
        card2 = self._p2.top()
        if card1 > card2:
            p1 = self._p1.win_round(card1, card2)
            p2 = self._p2.lose_round()
        else:
            p1 = self._p1.lose_round()
            p2 = self._p2.win_round(card2, card1)
        return Game(p1, p2)

    def play_game(self) -> "Game":
        game = self
        while game.winner is None:
            game = game.single_round()
        return game
