from common.utils import count
from typing import Generator


class Forrest:
    def __init__(self, trees: list[list[bool]]):
        self.trees = trees

    @property
    def width(self) -> int:
        return len(self.trees[0])

    @property
    def hight(self) -> int:
        return len(self.trees)

    def slope(self, right: int, down: int) -> "Slope":
        if down <= 0:
            raise Exception("negatives slopes are not allowed")

        return Slope(self, right, down)

    def is_tree(self, right: int, down: int) -> bool:
        return self.trees[down][right]


class Slope:
    def __init__(self, forrest: Forrest, right: int, down: int):
        self.forrest = forrest
        self.right = right
        self.down = down

    def __iter__(self) -> Generator[tuple[bool, int, int], None, None]:
        pos_h = 0
        pos_v = 0
        while pos_v < self.forrest.hight:
            yield (self.forrest.is_tree(pos_h, pos_v), pos_h, pos_v)
            pos_h = (pos_h + self.right) % self.forrest.width
            pos_v += self.down

    def count_trees(self) -> int:
        return count(self, lambda t: t[0])

    def draw(self) -> str:
        return "".join('#' if t else '.' for t, _, _ in self)


class Factory:
    @staticmethod
    def from_matrix(pattern: list[str]) -> Forrest:
        # Everyting that is not a gap is a tree (there are many kind of trees)
        trees = [[t != '.' for t in row] for row in pattern]

        if not trees[0] or any(len(row) != len(trees[0]) for row in trees):
            raise Exception("Illegal forrest description")

        return Forrest(trees)
