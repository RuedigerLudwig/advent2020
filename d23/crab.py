from typing import Optional
from .ring import Ring


class GameException(Exception):
    pass


class CrabGame:
    def __init__(self, ring: Ring[int]):
        self.ring = ring

    @staticmethod
    def from_string(input: str) -> "CrabGame":
        elements = dict[int, Ring]()

        mx = 0
        run: Optional[Ring[int]] = None
        for digit in input:
            if digit not in ('123456789'):
                raise GameException("Only digits from 1-9 are allowed")

            value = int(digit)
            mx = max(mx, value)
            run = Ring.create(value, run)
            elements[value] = run

        if run is None:
            raise GameException("Empty input is not allowed")

        if mx != len(run):
            raise GameException("Input must start at 1 and be continous")

        return CrabGame(run.next)

    def run(self, rounds: int) -> "CrabGame":
        current = self.ring.copy()
        references = {ring.value: ring for ring in current}
        highest = len(references)

        # This would blow our algorithm. We need at the very least 4 numbers
        # (and so few  would not really make sense either, but works anyway)
        if highest < 4:
            raise GameException("Need at least 4 numbers")

        for _ in range(rounds):
            pickup = current.next
            pickup_middle = pickup.next
            pickup_end = pickup_middle.next

            avoid = (pickup.value, pickup_middle.value, pickup_end.value)

            current_value = current.value
            dest_value = current_value - 1 if current_value != 1 else highest
            while dest_value in avoid:
                dest_value = dest_value - 1 if dest_value != 1 else highest

            destination = references[dest_value]

            current.next = pickup_end.next
            pickup_end.next = destination.next
            destination.next = pickup

            current = current.next

        return CrabGame(current)

    def pump_up_to(self, new_highest: int) -> "CrabGame":
        current = self.ring.copy()

        highest = len(current)
        if new_highest <= highest:
            return self

        run = current.prev()
        for value in range(highest, new_highest):
            run = run.append(value + 1)

        return CrabGame(current)

    def string_result(self, value: int) -> str:
        return str(self.ring[value])[1:]

    def tuple_result(self, value: int) -> tuple[int, int]:
        element = self.ring[value]
        return element.next.value, element.next.next.value


def play_game(input: str, rounds: int, min_elements: int = 0) -> CrabGame:
    game = CrabGame.from_string(input)
    game.pump_up_to(min_elements)
    return game.run(rounds)
