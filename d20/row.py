from .directions import Direction
from typing import Counter, Iterable, Optional

Edges = dict[Direction, "Row"]


class Row:
    def __init__(self, dots: Iterable[bool]):
        self._dots = list(dots)

    def __repr__(self) -> str:
        return "".join('#' if t else '.' for t in self._dots)

    def __str__(self) -> str:
        return "".join('#' if t else '.' for t in self._dots)

    def __eq__(self, other: "Row") -> bool:
        return all(t == o for t, o in zip(self._dots, other._dots))

    def __hash__(self) -> int:
        result = 37
        for p, t in enumerate(self._dots):
            if t:
                result ^= hash(p)
        return result

    def __getitem__(self, key: int) -> bool:
        return self._dots[key]

    def __len__(self) -> int:
        return len(self._dots)

    @property
    def dot_count(self) -> int:
        return Counter(self._dots)[True]

    def reverse(self) -> "Row":
        return Row(self._dots[::-1])

    @staticmethod
    def from_string(line: str) -> "Row":
        return Row(t == '#' for t in line.strip())

    def get_matching_row(self,
                         others: Edges) -> Optional[tuple[Direction, bool]]:
        reverse = self.reverse()
        for dir, other_edge in others.items():
            if other_edge == self:
                return dir, True
            if other_edge == reverse:
                return dir, False
        return None

    def shrink(self) -> "Row":
        return Row(self._dots[1:-1])

    @staticmethod
    def merge(lst: list[list["Row"]]) -> list["Row"]:
        def do_merge(row: Iterable[Row]) -> Row:
            result = list[bool]()
            for single in row:
                result = result + single._dots
            return Row(result)

        return [do_merge(row) for row in zip(*lst)]
