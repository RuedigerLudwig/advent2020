from collections import deque
from typing import Sequence

CardHand = tuple[int, ...]
HandTuple = tuple[CardHand, CardHand]


class AdvancedGame:
    def __init__(self, p1: Sequence[int], p2: Sequence[int]):
        self._p1 = tuple(p1)
        self._p2 = tuple(p2)

    def single_game(
            self, known_games: dict[HandTuple,
                                    bool]) -> tuple[Sequence[int], bool]:
        known_hand = set[HandTuple]()
        p1 = deque(self._p1)
        p2 = deque(self._p2)
        while len(p1) > 0 and len(p2) > 0:
            key = tuple(p1), tuple(p2)
            if key in known_hand:  # Prevent Recursion
                return p1, True
            known_hand.add(key)

            card1 = p1.popleft()
            card2 = p2.popleft()

            if card1 <= len(p1) and card2 <= len(p2):
                cards1 = tuple(p1[x] for x in range(card1))
                cards2 = tuple(p2[x] for x in range(card2))
                key = cards1, cards2

                p1_is_winner = known_games.get(key)
                if p1_is_winner is None:
                    _, p1_is_winner = AdvancedGame(
                        cards1, cards2).single_game(known_games)
                    known_games[key] = p1_is_winner
            else:
                p1_is_winner = card1 > card2

            if p1_is_winner:
                p1.extend([card1, card2])
            else:
                p2.extend([card2, card1])

        if len(p1) != 0:
            return p1, True
        else:
            return p2, False

    def play_game(self) -> tuple[Sequence[int], bool]:
        known_games = dict[HandTuple, bool]()
        return self.single_game(known_games)
