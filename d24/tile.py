from enum import Enum
from typing import Iterable

Vector = tuple[int, int]
Walk = Iterable["Dir"]


class Dir(Enum):
    East = (1, 0)
    NorthEast = (0, 1)
    NorthWest = (-1, 1)
    West = (-1, 0)
    SouthWest = (0, -1)
    SouthEast = (1, -1)

    @staticmethod
    def from_str(word: str) -> "Dir":
        return _DIR_WORDS[word]


_DIR_WORDS = {
    "e": Dir.East,
    "ne": Dir.NorthEast,
    "nw": Dir.NorthWest,
    "w": Dir.West,
    "sw": Dir.SouthWest,
    "se": Dir.SouthEast
}


def add_vectors(first: Vector, second: Vector) -> Vector:
    return first[0] + second[0], first[1] + second[1]


def get_adjacent(tile: Vector) -> set[Vector]:
    return {add_vectors(tile, dir.value) for dir in list(Dir)}


class TileFactory:
    @staticmethod
    def parse_walk(line: str) -> Walk:
        try:
            it = iter(line.strip())
            while True:
                word = next(it)
                if word in ('s', 'n'):
                    word += next(it)
                yield Dir.from_str(word)
        except StopIteration:
            pass

    @staticmethod
    def parse_floor(walks: Iterable[Walk]) -> "Floor":
        floor = set[Vector]()
        for walk in walks:
            tile = TileFactory.walk_to_tile(walk)
            if tile in floor:
                floor.remove(tile)
            else:
                floor.add(tile)
        return Floor(floor)

    @staticmethod
    def parse_lines(lines: list[str]) -> "Floor":
        return TileFactory.parse_floor(
            TileFactory.parse_walk(line) for line in lines)

    @staticmethod
    def walk_to_tile(walk: Walk, start: Vector = (0, 0)) -> Vector:
        result = start
        for dir in walk:
            result = add_vectors(result, dir.value)
        return result


class Floor:
    def __init__(self, tiles: set[Vector]):
        self.tiles = tiles

    def count_tiles(self) -> int:
        return len(self.tiles)

    def simulate(self, days: int):
        def relevant(tiles: set[Vector]) -> set[Vector]:
            result = set(tiles)
            for tile in tiles:
                result |= get_adjacent(tile)
            return result

        tiles = self.tiles
        for _ in range(days):
            next_day = set[Vector]()

            for tile in relevant(tiles):
                num_neighbors = len(tiles & get_adjacent(tile))

                if tile in tiles:
                    if num_neighbors in (1, 2):
                        next_day.add(tile)
                elif num_neighbors == 2:
                    next_day.add(tile)

            tiles = next_day

        return Floor(tiles)
