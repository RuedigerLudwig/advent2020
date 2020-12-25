class Player:
    def __init__(self, cards: tuple[int]):
        self._cards = cards

    def __eq__(self, other: "Player") -> bool:
        return self._cards == other._cards

    def __hash__(self) -> int:
        return hash(self._cards)

    def __repr__(self) -> str:
        return ",".join(str(s) for s in self._cards)

    @property
    def cards(self):
        return self._cards

    @property
    def num_cards(self) -> int:
        return len(self._cards)

    def top(self) -> int:
        if len(self._cards) == 0:
            raise Exception
        return self._cards[0]

    def win_round(self, card1: int, card2: int) -> "Player":
        new_cards: tuple[int, ...] = *self._cards[1:], card1, card2
        return Player(new_cards)

    def lose_round(self) -> "Player":
        return Player(tuple(self._cards[1:]))

    def has_lost(self) -> bool:
        return len(self._cards) == 0

    @property
    def card_value(self) -> int:
        return sum(p * v for p, v in enumerate(reversed(self._cards), 1))
