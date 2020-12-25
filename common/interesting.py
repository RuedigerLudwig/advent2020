from itertools import tee
from typing import Generator, Iterable, TypeVar

_T = TypeVar("_T")


def combinations(iter: Iterable[_T],
                 count: int) -> Generator[tuple[_T, ...], None, None]:
    if count == 1:
        for t in iter:
            yield t,

    else:
        try:
            while True:
                iter, snd = tee(iter)
                head = next(iter)
                _ = next(snd)
                for p in combinations(snd, count - 1):
                    yield head, *p
        except StopIteration:
            pass
