from pathlib import Path, PurePath
from typing import Iterable, Optional, TypeVar, Callable
from common.timer import Timer  # type: ignore # noqa: F401

T = TypeVar('T')


def read_file(
    name: str, convert: Callable[[str], Optional[T]] = lambda x: x.strip()
) -> list[T]:
    with open(Path.cwd() / PurePath(name), "rt") as f:
        return [
            r for r in (convert(line) for line in f.readlines())
            if r is not None
        ]


def some_filter(lst: Iterable[Optional[T]]) -> Iterable[T]:
    return (item for item in lst if item is not None)


def count(lst: Iterable[T], check: Callable[[T], bool]) -> int:
    return sum(1 for t in lst if check(t))


def safe_int(s: str) -> Optional[int]:
    try:
        return int(s)
    except ValueError:
        return None


def safe_get(lst: list[T], pos: int, default: T) -> T:
    try:
        return lst[pos]
    except IndexError:
        return default
