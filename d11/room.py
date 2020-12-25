import copy
from collections import Counter
from typing import Optional

Seat = Optional[bool]


class Room:
    def __init__(self, rows: list[list[Seat]]):
        self.rows = rows

    def __eq__(self, other: "Room") -> bool:
        for row, orow in zip(self.rows, other.rows):
            for seat, oseat in zip(row, orow):
                if seat != oseat:
                    return False
        return True

    def row_count(self):
        return len(self.rows)

    def col_count(self):
        return len(self.rows[0])

    def get_seat(self, row: int, col: int) -> Seat:
        try:
            return self.rows[row][col]
        except IndexError:
            return None

    def count_neighbours(self, row: int, col: int) -> int:
        result = 0
        for r in range(max(0, row - 1), min(self.row_count(), row + 2)):
            for c in range(max(0, col - 1), min(self.col_count(), col + 2)):
                if self.rows[r][c]:
                    result += 1
        return result

    def count_other_neighbours(self, row: int, col: int) -> int:
        result = 0
        for r in (-1, 0, 1):
            for c in (-1, 0, 1):
                if r != 0 or c != 0:
                    space: Seat = None
                    curr_row = row + r
                    curr_col = col + c
                    while (space is None and 0 <= curr_row < self.row_count()
                           and 0 <= curr_col < self.col_count()):
                        space = self.rows[curr_row][curr_col]
                        curr_row += r
                        curr_col += c
                    if space:
                        result += 1
        return result

    def count_seats(self):
        c = Counter(s for row in self.rows for s in row)
        return c[True]

    def simulate(self) -> "Room":
        next_room = copy.deepcopy(self.rows)
        for r in range(self.row_count()):
            for c in range(self.col_count()):
                seat = self.get_seat(r, c)
                if seat is not None:
                    neighbors = self.count_neighbours(r, c)
                    if (seat and neighbors >= 5) or (not seat
                                                     and neighbors != 0):
                        next_room[r][c] = False
                    else:
                        next_room[r][c] = True
        result = Room(next_room)
        return result

    def simulate_to_fixed(self) -> "Room":
        last = self
        finished = False
        while not finished:
            next_room = last.simulate()
            finished = next_room == last
            last = next_room
        return last

    def simulate2(self) -> "Room":
        next_room = copy.deepcopy(self.rows)
        for r in range(self.row_count()):
            for c in range(self.col_count()):
                seat = self.get_seat(r, c)
                if seat is not None:
                    neighbors = self.count_other_neighbours(r, c)
                    if (seat and neighbors >= 5) or (not seat
                                                     and neighbors != 0):
                        next_room[r][c] = False
                    else:
                        next_room[r][c] = True
        return Room(next_room)

    def simulate_to_fixed2(self) -> "Room":
        last = self
        finished = False
        while not finished:
            next_round = last.simulate2()
            if next_round == last:
                finished = True
            last = next_round

        return last


class Factory:
    @staticmethod
    def from_string(seats: str) -> list[Seat]:
        def get_seat(s: str) -> Optional[bool]:
            if s == '#':
                return True
            elif s == 'L':
                return False
            return None

        return [get_seat(s) for s in seats.strip()]

    @staticmethod
    def from_lines(lines: list[str]) -> Room:
        return Room([Factory.from_string(line) for line in lines])
