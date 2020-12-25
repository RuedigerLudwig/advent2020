from typing import Tuple, Callable

Coord = Tuple[int, int]


class Ferry(object):
    def __init__(self, position: Coord, face: str) -> None:
        self.position = position
        self.face = face

    def __str__(self) -> str:
        pos = f"ferry: ({self.position})"
        face = f"facing: ({self.face})"
        return pos + ", " + face

    def _move_north(self, distance: int) -> "Ferry":
        return Ferry((self.position[0], self.position[1] + distance), self.face)

    def _move_south(self, distance: int) -> "Ferry":
        return Ferry((self.position[0], self.position[1] - distance), self.face)

    def _move_east(self, distance: int) -> "Ferry":
        return Ferry((self.position[0] + distance, self.position[1]), self.face)

    def _move_west(self, distance: int) -> "Ferry":
        return Ferry((self.position[0] - distance, self.position[1]), self.face)

    def _move_left(self, distance: int) -> "Ferry":
        dirs = "ENWSENWS"
        tick = distance // 90
        pos = dirs.find(self.face)
        return Ferry(self.position, dirs[pos + tick])

    def _move_right(self, distance: int) -> "Ferry":
        dirs = "ESWNESWN"
        tick = distance // 90
        pos = dirs.find(self.face)
        return Ferry(self.position, dirs[pos + tick])

    def _move_forward(self, distance: int) -> "Ferry":
        action: dict[str, Callable[[int], "Ferry"]] = {
            "S": self._move_south,
            "E": self._move_east,
            "N": self._move_north,
            "W": self._move_west,
        }
        return action[self.face](distance)

    def move(self, direction: str, distance: int) -> "Ferry":
        action: dict[str, Callable[[int], "Ferry"]] = {
            "S": self._move_south,
            "E": self._move_east,
            "N": self._move_north,
            "W": self._move_west,
            "L": self._move_left,
            "R": self._move_right,
            "F": self._move_forward,
        }
        return action[direction](distance)
