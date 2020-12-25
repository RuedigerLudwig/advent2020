from typing import Iterable, Optional
from itertools import combinations, islice


def _check_combinations(lst: Iterable[int], expected: int) -> bool:
    for combi in combinations(lst, 2):
        if sum(combi) == expected:
            return True
    return False


def get_incorrect_pos(stream: list[int], preamble: int) -> Optional[int]:
    for window in range(preamble, len(stream)):
        if not _check_combinations(islice(stream, window - preamble, window),
                                   stream[window]):
            return window
    return None


def get_weakness(stream: list[int], incorrect_pos: int) -> Optional[list[int]]:
    expected = stream[incorrect_pos]
    for size in range(2, incorrect_pos):
        for start in range(0, incorrect_pos - size - 2):
            lst = islice(stream, start, start + size)
            if sum(lst) == expected:
                return stream[start:start + size]
    return None
