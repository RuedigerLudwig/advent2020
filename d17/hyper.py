from typing import Generator, Iterable, Optional
import itertools

Coord = tuple[int, ...]


class Hyper:
    _INACTIVE = '.'
    _ACTIVE = '#'

    @staticmethod
    def parse_from_2D(rows: list[str], dim: int) -> "HyperSpace":
        rest = [0 for _ in range(2, dim)]

        space = set[Coord]()
        for y, row in enumerate(rows):
            for x, cube in enumerate(row):
                if cube == Hyper._ACTIVE:
                    space.add((x, y, *rest))
        return HyperSpace(space, dim)

    @staticmethod
    def print_cube(active: bool) -> str:
        return Hyper._ACTIVE if active else Hyper._INACTIVE


class HyperSpace:
    def __init__(self, cubes: set[Coord], dim: int):
        self._cubes = cubes
        self._dim = dim

    def count_active(self):
        return len(self._cubes)

    def print(self) -> list[str]:
        names = "zwvut"
        result = list[str]()

        ranges = list(
            itertools.product(*[
                range(*self._get_range_for_dim(dim))
                for dim in range(self._dim - 1, 1, -1)
            ]))

        for slice in ranges:
            if result:
                result.append("")
            result.append(", ".join(f"{names[p]}={v}"
                                    for p, v in enumerate(reversed(slice))))
            result.extend([
                "".join(
                    Hyper.print_cube((x, y, *slice) in self._cubes)
                    for x in range(*self._get_range_for_dim(0)))
                for y in range(*self._get_range_for_dim(1))
            ])
        return result

    def run(self, steps: int) -> "HyperSpace":
        def check_for_changes(
                to_check: set[Coord],
                cubes: set[Coord]) -> Generator[Coord, None, None]:
            for coord in to_check:
                state = coord in cubes
                active = cubes.intersection(
                    Delta.get_all_neighbors(coord, self._dim))
                neighbors = len(active)
                if state:
                    if neighbors not in (2, 3):
                        yield coord  # Dying
                elif neighbors == 3:
                    yield coord  # Being born

        space = self._cubes
        changed: Optional[set[Coord]] = None
        for _ in range(steps):
            to_check = HyperSpace._expand_cubes(changed or space, self._dim)
            changed = set(check_for_changes(to_check, space))
            space = space.symmetric_difference(changed)

        return HyperSpace(space, self._dim)

    def _get_range_for_dim(self, dim: int) -> tuple[int, int]:
        return HyperSpace._minmax(c[dim] for c in self._cubes)

    @staticmethod
    def _minmax(iterable: Iterable[int]) -> tuple[int, int]:
        it = iter(iterable)
        mn = next(it)
        mx = mn
        for n in it:
            mn = min(n, mn)
            mx = max(n, mx)
        return mn, mx + 1

    @staticmethod
    def _expand_cubes(changed: set[Coord], dim: int) -> set[Coord]:
        result = set[Coord]()
        for coord in changed:
            result.update(Delta.get_all_neighbors(coord, dim))
        return result


class Delta:
    _deltas = dict[int, list[tuple[int, ...]]]()

    @staticmethod
    def get_all_neighbors(coord: Coord,
                          dim: int) -> Generator[Coord, None, None]:
        yield from (Delta._add_delta(coord, delta)
                    for delta in Delta._get_delta_for(dim))

    @staticmethod
    def _get_delta_for(dim: int):
        result = Delta._deltas.get(dim)
        if not result:
            near = [(-1, 0, 1) for _ in range(dim)]
            result = [
                delta for delta in itertools.product(*near) if any(delta)
            ]
            Delta._deltas[dim] = result
        return result

    @staticmethod
    def _add_delta(coord: Coord, delta: Coord) -> Coord:
        return tuple(c + d for c, d in zip(coord, delta))
