from typing import Generator
from collections import Counter


def get_differences(adapters: list[int]) -> int:
    def diff_generator(lst: list[int]) -> Generator[int, None, None]:
        last = 0
        for current in lst:
            yield current - last
            last = current

    diffs = Counter(diff_generator(sorted(adapters)))
    return (diffs[3] + 1) * diffs[1]


def get_num_arrangements(adapters: list[int]) -> int:
    adapters = [0] + sorted(adapters)
    variants = {0: 1, adapters[1]: 1}
    for i in range(2, len(adapters)):
        current = adapters[i]
        sucessors = (adapters[j] for j in range(max(0, i - 3), i)
                     if current - adapters[j] <= 3)
        variants[current] = sum(variants[s] for s in sucessors)
    return variants[adapters[-1]]
