import re
from typing import Callable, Optional, Generator

_mask_pattern = re.compile(r"^mask = (?P<mask>[X10]{36})")
_mem_pattern = re.compile(r"mem\[(?P<addr>\d+)] = (?P<value>\d+)")


def get_mask(line: str) -> list[Optional[int]]:
    def get_num(item: str) -> Optional[int]:
        if item == '1':
            return 1
        if item == '0':
            return 0
        return None

    match = _mask_pattern.match(line)
    if match is None:
        raise Exception("Not a valid mask")
    return [get_num(c) for c in match["mask"]]


def get_mem(line: str) -> tuple[int, int]:
    match = _mem_pattern.match(line)
    if match is None:
        raise Exception("Not a valid mem")
    return int(match["addr"]), int(match["value"])


def apply_mask(mask: list[Optional[int]], value: int) -> int:
    result = 0
    length = len(mask) - 1
    for pos in range(length, -1, -1):
        item = mask[pos]
        if item is not None:
            result += item << (length - pos)
        else:
            result += value % 2 << (length - pos)
        value >>= 1
    return result


def run_version_1(lines: list[str]) -> int:
    def version_1(addr: int, value: int,
                  mask: list[Optional[int]]) -> dict[int, int]:
        return {addr: apply_mask(mask, value)}

    return _run(lines, version_1)


def _lst_to_number(lst: list[int]) -> int:
    result: int = 0

    for i in lst:
        result <<= 1
        result += i
    return result


def get_possible_values(lst: list[Optional[int]]) -> list[int]:
    def get_next(lst: list[Optional[int]],
                 pos: int) -> Generator[list[int], None, None]:
        while pos >= 0 and lst[pos] is not None:
            pos -= 1

        if pos < 0:
            yield lst  # type: ignore
        else:
            next_lst = lst.copy()
            for b in (0, 1):
                next_lst[pos] = b
                yield from get_next(next_lst, pos - 1)

    return [_lst_to_number(p) for p in get_next(lst, len(lst) - 1)]


def apply_floating_mask(mask: list[Optional[int]], value: int) -> list[int]:
    result = mask.copy()
    for pos in range(len(mask) - 1, -1, -1):
        if mask[pos] == 0:
            result[pos] = value % 2
        value >>= 1

    return get_possible_values(result)


def run_version_2(lines: list[str]) -> int:
    def version_2(addr: int, value: int,
                  mask: list[Optional[int]]) -> dict[int, int]:
        return {ad: value for ad in apply_floating_mask(mask, addr)}

    return _run(lines, version_2)


def _run(
        lines: list[str], call: Callable[[int, int, list[Optional[int]]],
                                         dict[int, int]]) -> int:
    mask = list[Optional[int]]()
    results = dict[int, int]()

    for line in lines:
        if line.startswith("mask"):
            mask = get_mask(line)
        else:
            addr, value = get_mem(line)
            results.update(call(addr, value, mask))

    return sum(results.values())
