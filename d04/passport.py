from typing import Generator, Iterable

Passport = dict[str, str]


class Factory:
    @staticmethod
    def _get_chunks(lines: list[str]) -> Generator[dict[str, str], None, None]:
        result = dict[str, str]()
        for line in lines:
            if line:
                for part in line.split():
                    [key, value] = part.split(':')
                    result[key] = value
            else:
                yield result
                result = dict[str, str]()
        yield result

    @staticmethod
    def from_string(lines: list[str]) -> Iterable[Passport]:
        return Factory._get_chunks(lines)
