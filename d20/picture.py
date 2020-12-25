from typing import Iterable
from .row import Row
from .helper import Helper
from .tile import Tile
from .directions import Direction


class Picture:
    def __init__(self, tiles: Iterable[Tile]):
        self.tiles = set(tiles)

    def get_dict_by_edge_dots(self) -> dict[int, set[Tile]]:
        result = dict[int, set[Tile]]()
        for tile in self.tiles:
            for edge in tile.edges.values():
                bag = result.setdefault(edge.dot_count, set[Tile]())
                bag.add(tile)
        return result

    def get_posible_connections(
            self) -> dict[Tile, list[tuple[Tile, Direction]]]:
        et_dict = self.get_dict_by_edge_dots()

        result = dict[Tile, list[tuple[Tile, Direction]]]()

        for tile in self.tiles:
            for edge_dir, edge in tile.edges.items():
                for candidate in tile.find_fitting(et_dict[edge.dot_count],
                                                   edge_dir):
                    bag = result.setdefault(tile, list[tuple[Tile,
                                                             Direction]]())
                    bag.append((candidate, edge_dir))
        return result

    def __getitem__(self, number: int) -> Tile:
        for tile in self.tiles:
            if tile.number == number:
                return tile
        raise IndexError

    def get_corners(self) -> list[Tile]:
        return [
            number
            for number, neighbors in self.get_posible_connections().items()
            if len(neighbors) == 2
        ]

    def get_ordered(self):
        possible = self.get_posible_connections()
        corner, fitting_neighbors = next(
            (number, neighbors) for number, neighbors in possible.items()
            if len(neighbors) == 2)

        neighbor_edges = tuple(n[1] for n in fitting_neighbors)
        corner = corner.rotate_north_west(*neighbor_edges)

        size = None

        result = list[list[Tile]]()
        current_row = list[Tile]()
        result.append(current_row)
        current_row.append(corner)

        last_element = corner
        next_dir = Direction.EAST

        finished = False
        while not finished:
            neighbors = [n[0] for n in possible[last_element]]
            fitting_neighbors = last_element.find_fitting(neighbors, next_dir)
            if len(fitting_neighbors) != 1:
                raise Exception
            neighbor = fitting_neighbors.pop()
            fitted = last_element.fit_tile(neighbor, next_dir)
            if fitted is None:
                raise Exception

            current_row.append(fitted)

            if ((size is None and len(possible[fitted]) == 2)  # NE-Corner
                    or len(current_row) == size):
                size = size or len(current_row)
                if len(result) >= size:
                    finished = True
                else:
                    last_element = current_row[0]
                    next_dir = Direction.SOUTH
                    current_row = list[Tile]()
                    result.append(current_row)
            else:
                last_element = fitted
                next_dir = Direction.EAST

        return result

    def as_image(self) -> list[Row]:
        ordered = self.get_ordered()
        shrunken = [[t.shrink() for t in row] for row in ordered]
        result = list[Row]()
        for row in shrunken:
            result.extend(Row.merge(row))
        return result

    def apply_monster(self, monster: list[Row]) -> tuple[int, int, int]:
        image = self.as_image()
        monster_info = Helper.convert_monster(monster)
        found = 0
        for _ in range(2):
            for _ in range(4):
                image = Helper.rotate(image, 1, False)
                found_here = Helper.check_for_monsters(image, monster_info)
                found += len(found_here)
            image = Helper.rotate(image, 0, True)
        dot_count = sum(row.dot_count for row in image)

        return dot_count, dot_count - found * len(monster_info[0]), found
