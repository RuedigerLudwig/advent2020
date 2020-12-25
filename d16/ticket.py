import re
from typing import Generator, Iterator

Range = tuple[int, int]
FieldDict = dict[str, tuple[Range, Range]]


class NoteSheet():
    desc_pattern = re.compile(r"^(?P<name>[^:]+): (?P<from1>\d+)-(?P<to1>\d+) "
                              r"or (?P<from2>\d+)-(?P<to2>\d+)")

    def __init__(self, lines: list[str]):
        # Fields
        line_iterator = iter(lines)
        fields = FieldDict(NoteSheet._process_fields(line_iterator))

        next(line_iterator)  # your ticket:
        my_ticket_numbers = NoteSheet._list_to_numbers(next(line_iterator))

        next(line_iterator)  #
        next(line_iterator)  # nearby tickets:

        nearby_numbers = [
            NoteSheet._list_to_numbers(line) for line in line_iterator
        ]

        self.fields = fields
        self.my_ticket_numbers = my_ticket_numbers
        self.nearby_numbers = nearby_numbers

    @staticmethod
    def _process_fields(
        iterator: Iterator[str]
    ) -> Generator[tuple[str, tuple[Range, Range]], None, None]:
        for field in iterator:
            match = NoteSheet.desc_pattern.match(field)
            if not match:
                return None

            yield (match["name"], ((int(match["from1"]), int(match["to1"])),
                                   (int(match["from2"]), int(match["to2"]))))

    @staticmethod
    def _list_to_numbers(line: str) -> list[int]:
        return [int(i) for i in line.split(",")]

    @staticmethod
    def _matches(value: int, ranges: tuple[Range, Range]) -> bool:
        return (ranges[0][0] <= value <= ranges[0][1]
                or ranges[1][0] <= value <= ranges[1][1])

    def find_possible_fields(self, numbers: list[int]) -> list[set[str]]:
        return [{
            name
            for name, ranges in self.fields.items()
            if NoteSheet._matches(num, ranges)
        } for num in numbers]

    def find_invalid_numbers(self) -> Generator[int, None, None]:
        for nearby in self.nearby_numbers:
            matching = self.find_possible_fields(nearby)
            yield from (num for num, possible in zip(nearby, matching)
                        if not possible)

    def is_valid_ticket(self, ticket: dict[str, int]) -> bool:
        return all(
            self._matches(value, self.fields[name])
            for name, value in ticket.items())


class TicketMatcher:
    def __init__(self, notes: NoteSheet):
        fields = [set(notes.fields.keys()) for _ in range(len(notes.fields))]

        # Collect
        for current_nearby in notes.nearby_numbers:
            possible_fields = notes.find_possible_fields(current_nearby)
            if all(possible_fields):
                for field_set, possible_set in zip(fields, possible_fields):
                    field_set &= possible_set

        # Reduce
        while any(len(f) > 1 for f in fields):
            changed = False
            for field_set in fields:
                if len(field_set) == 1:
                    for field_set_2 in fields:
                        if field_set < field_set_2:
                            field_set_2 -= field_set
                            changed = True

            if not changed:
                raise Exception("Could not reduce to single field")

        # Throws error if any set is empty
        self.fields = [f.pop() for f in fields]
        self._notes = notes

    def make_ticket(self, ticket: list[int]) -> dict[str, int]:
        return dict(zip(self.fields, ticket))

    def are_valid_numbers(self, numbers: list[int]) -> bool:
        return self._notes.is_valid_ticket(self.make_ticket(numbers))
