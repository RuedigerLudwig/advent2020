from enum import Enum
from typing import Union


class Direction(Enum):
    EAST = 0
    NORTH = 1
    WEST = 2
    SOUTH = 3

    def __add__(self, to_add: Union[int, "Direction"]) -> "Direction":
        if isinstance(to_add, int):
            val: int = (self.value + to_add) % 4
        else:
            val: int = (self.value + to_add.value) % 4
        return Direction(val)

    def __sub__(self, to_sub: Union[int, "Direction"]) -> "Direction":
        if isinstance(to_sub, int):
            val: int = (self.value - to_sub) % 4
        else:
            val: int = (self.value - to_sub.value) % 4
        return Direction(val)

    def __radd__(self, to_add: int) -> "Direction":
        return self + to_add

    def __rsub__(self, to_sub: int) -> "Direction":
        val: int = (to_sub - self.value) % 4
        return Direction(val)

    def is_horizontal(self) -> bool:
        return self is Direction.EAST or self is Direction.WEST

    def is_vertical(self) -> bool:
        return self is Direction.NORTH or self is Direction.SOUTH
