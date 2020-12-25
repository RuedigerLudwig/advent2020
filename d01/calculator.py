from typing import Optional


def find(lst: list[int], expected: int, count: int) -> Optional[list[int]]:
    if not lst or count <= 0:
        return None

    if count == 1:
        if expected in lst:
            return [expected]
        else:
            return None

    head, *tail = lst
    rest = expected - head

    result = find(tail, rest, count - 1)
    if result is not None:
        return [head] + result

    return find(tail, expected, count)
