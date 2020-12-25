from typing import Iterable, Optional
from .directions import Direction
from .row import Edges, Row
from .helper import Helper


class Tile:
    def __init__(self, number: int, rows: list[Row]):
        self.number = number
        self.rows = rows

        self.edges: Edges = {
            Direction.EAST: Row(row[-1] for row in self.rows).reverse(),
            Direction.NORTH: self.rows[0].reverse(),
            Direction.WEST: Row(row[0] for row in self.rows),
            Direction.SOUTH: self.rows[-1],
        }

    def __repr__(self):
        return f"Tile({self.number})"

    def as_list(self) -> list[str]:
        return [f"Tile {self.number}:"] + [str(row) for row in self.rows]

    def as_str(self) -> str:
        return "\n".join(self.as_list())

    def print(self):
        for line in self.as_list():
            print(line)
        print()

    def __eq__(self, other: "Tile"):
        return self.number == other.number

    def __hash__(self):
        return hash(self.number)

    def fit_tile(self, second: "Tile",
                 from_dir: Direction) -> Optional["Tile"]:
        edge = self.edges[from_dir]
        match = edge.get_matching_row(second.edges)
        if match is None:
            return None

        curr_dir, flip = match
        to_dir = from_dir + 2

        if flip and to_dir.is_horizontal():
            turns: int = (to_dir - curr_dir + 2).value
        else:
            turns: int = (to_dir - curr_dir).value

        return second.rotate_tile(turns, flip)

    def rotate_tile(self, turns: int, flip: bool) -> "Tile":
        return Tile(self.number, Helper.rotate(self.rows, turns, flip))

    def rotate_north_west(self, first_dir: Direction,
                          second_dir: Direction) -> "Tile":
        turns = (4 - first_dir).value
        if turns != 0:
            turned = self.rotate_tile(turns, False)
            second_dir = second_dir + turns
        else:
            turned = self

        if second_dir.is_horizontal():
            raise Exception

        if second_dir is Direction.NORTH:
            turned = turned.rotate_tile(3, False)

        return turned

    def find_fitting(self, candidates: Iterable["Tile"],
                     dir: Direction) -> set["Tile"]:
        edge = self.edges[dir]
        return {
            candidate
            for candidate in candidates if candidate != self
            and edge.get_matching_row(candidate.edges) is not None
        }

    def shrink(self) -> list[Row]:
        return [row.shrink() for row in self.rows[1:-1]]
