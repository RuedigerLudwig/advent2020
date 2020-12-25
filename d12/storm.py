from .waypoint import WaypointFerry
from .ferry import Ferry
from typing import Tuple
import re

Action = Tuple[str, int]


class StormFactory(object):
    pattern = re.compile(r"^(?P<dir>[NSEWLRF])(?P<dist>\d+)$")

    @staticmethod
    def from_string(action: str) -> Action:
        match = StormFactory.pattern.match(action)
        if not match:
            raise Exception(f"Not a valid action: {action}")
        return match["dir"], int(match["dist"])

    @staticmethod
    def get_distance(lst: list[Action]) -> int:
        ferry = Ferry((0, 0), "E")
        for action in lst:
            ferry = ferry.move(*action)
        return StormFactory.manhattan_distance(*ferry.position)

    @staticmethod
    def get_waypoint_distance(lst: list[Action]) -> int:
        ferry = WaypointFerry((0, 0), (10, 1))
        for action in lst:
            ferry = ferry.move(*action)
        return StormFactory.manhattan_distance(*ferry.position)

    @staticmethod
    def manhattan_distance(pos_x: int, pos_y: int):
        return abs(pos_x) + abs(pos_y)
