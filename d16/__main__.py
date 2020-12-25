from common.utils import read_file, count
from .ticket import NoteSheet, TicketMatcher
import math


def main() -> None:
    lines = read_file("d16/data/input.txt")
    notes = NoteSheet(lines)

    # Part 1
    invalid = notes.find_invalid_numbers()
    print(f"The error rate is 1-> {sum(invalid)} <-1")

    # Blubber
    matcher = TicketMatcher(notes)

    my_ticket = matcher.make_ticket(notes.my_ticket_numbers)
    output = " ,".join(f"'{name}': {my_ticket[name]}"
                       for name in sorted(my_ticket.keys()))
    print(f"My Ticket is: {output}")
    print(f"Is it valid? {notes.is_valid_ticket(my_ticket)}")

    num = count(notes.nearby_numbers, lambda n: matcher.are_valid_numbers(n))
    print(f"There are {num} valid tickets nearby")

    # Part 2
    magic = (v for k, v in my_ticket.items() if k.startswith("departure"))
    print(f"My magic ticket is 2-> {math.prod(magic)} <-2")


if __name__ == "__main__":
    main()
