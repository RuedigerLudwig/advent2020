import re


class Factory:
    _pattern = re.compile(r"^([FB]{7}[RL]{3})$")

    @staticmethod
    def from_string(input: str) -> int:
        match = Factory._pattern.match(input)
        if match is None:
            raise Exception(f"Not a legal seat: {input}")

        id = 0
        for c in match[1]:
            id <<= 1
            if c in "BR":
                id ^= 1
        return id

    @staticmethod
    def find_missing(seats: list[int]) -> int:
        for id in range(min(seats) + 1, max(seats)):
            if id not in seats:
                return id
        raise Exception("This is not your flight")
