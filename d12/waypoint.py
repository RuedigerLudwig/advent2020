from typing import Callable

Coord = tuple[int, int]


class WaypointFerry:
    def __init__(self, position: Coord, waypoint: Coord):
        self.position = position
        self.waypoint = waypoint

    def __str__(self) -> str:
        ferry = f"ferry: ({self.position})"
        waypoint = f"waypoint: ({self.waypoint})"
        return ferry + ", " + waypoint

    def _move_north(self, distance: int) -> "WaypointFerry":
        return WaypointFerry(self.position,
                             (self.waypoint[0], self.waypoint[1] + distance))

    def _move_south(self, distance: int) -> "WaypointFerry":
        return WaypointFerry(self.position,
                             (self.waypoint[0], self.waypoint[1] - distance))

    def _move_east(self, distance: int) -> "WaypointFerry":
        return WaypointFerry(self.position,
                             (self.waypoint[0] + distance, self.waypoint[1]))

    def _move_west(self, distance: int) -> "WaypointFerry":
        return WaypointFerry(self.position,
                             (self.waypoint[0] - distance, self.waypoint[1]))

    def _move_left(self, distance: int) -> "WaypointFerry":
        tick = distance // 90
        waypoint = self.waypoint
        for _ in range(tick):
            waypoint = -waypoint[1], waypoint[0]
        return WaypointFerry(self.position, waypoint)

    def _move_right(self, distance: int) -> "WaypointFerry":
        tick = distance // 90
        waypoint = self.waypoint
        for _ in range(tick):
            waypoint = waypoint[1], -waypoint[0]
        return WaypointFerry(self.position, waypoint)

    def _move_forward(self, distance: int) -> "WaypointFerry":
        return WaypointFerry((self.position[0] + distance * self.waypoint[0],
                              self.position[1] + distance * self.waypoint[1]),
                             self.waypoint)

    def move(self, direction: str, distance: int) -> "WaypointFerry":
        action: dict[str, Callable[[int], "WaypointFerry"]] = {
            "S": self._move_south,
            "E": self._move_east,
            "N": self._move_north,
            "W": self._move_west,
            "L": self._move_left,
            "R": self._move_right,
            "F": self._move_forward,
        }
        return action[direction](distance)
