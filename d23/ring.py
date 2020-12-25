from typing import Generator, Generic, Optional, TypeVar

_T = TypeVar("_T")


class Ring(Generic[_T]):
    def __init__(self, value: _T, next_: "Ring[_T]"):
        self.value = value
        self.next = next_

    def copy(self) -> "Ring[_T]":
        result = None
        run = self
        first = True
        while first or run != self:
            first = False
            result = Ring.create(run.value, result)
            run = run.next

        if result is None:
            raise Exception  # Can actually never happen
        return result.next

    def __str__(self) -> str:
        result = str(self.value)
        run = self.next
        while run != self:
            result += str(run.value)
            run = run.next
        return result

    def __repr__(self) -> str:
        return f"Ring({self.value})"

    def __contains__(self, item: _T) -> bool:
        return self.find(item) is not None

    def __iter__(self) -> Generator["Ring[_T]", None, None]:
        run = self
        while run.next != self:
            yield run
            run = run.next
        yield run

    def __next__(self) -> "Ring[_T]":
        return self.next

    def __len__(self) -> int:
        run = self
        len = 0
        while run.next != self:
            len += 1
            run = run.next
        return len + 1

    def __getitem__(self, item: _T) -> "Ring[_T]":
        result = self.find(item)
        if result is None:
            raise KeyError(f"{item} is not in this ring")
        return result

    def append(self, value: _T) -> "Ring[_T]":
        ring = Ring[_T](value, self.next)
        self.next = ring
        return ring

    def find(self, value: _T) -> Optional["Ring[_T]"]:
        run = self
        while run.value != value and run.next != self:
            run = run.next
        if run.value == value:
            return run
        else:
            return None

    def prev(self) -> "Ring[_T]":
        run = self
        while run.next != self:
            run = run.next
        return run

    @staticmethod
    def create(value: _T, prev: Optional["Ring[_T]"]) -> "Ring[_T]":
        if prev is not None:
            return prev.append(value)

        # Mini Ring, points to itself
        ring: Ring[_T] = Ring[_T](value, None)  # type: ignore
        ring.next = ring
        return ring
