from common.utils import count
from typing import Iterable, Optional

Coord = tuple[int, int]
Seats = dict[Coord, "Seat"]


class Seat:
    def __init__(self, pos: Coord, occupied: bool, neighbors: list[Coord]):
        self.pos = pos
        self.occupied = occupied
        self.neighbors = neighbors

    def __eq__(self, other: "Seat") -> bool:
        return (self.pos == other.pos and self.occupied == other.occupied)

    def __repr__(self) -> str:
        return f"{RoomFactory.seat_char(self.occupied)} -> {self.neighbors}"


class Room:
    def __init__(self, row_count: int, col_count: int, seats: Seats):
        self._row_count = row_count
        self._col_count = col_count
        self._seats = seats

    def __eq__(self, other: "Room") -> bool:
        return (self._row_count == other._row_count
                and self._col_count == other._col_count
                and self._seats == other._seats)

    def __repr__(self) -> str:
        return "\n".join(self.print())

    def row_count(self):
        return self._row_count

    def col_count(self):
        return self._col_count

    def get_seat(self, row: int, col: int) -> Optional[bool]:
        seat = self._seats.get((row, col))
        if seat is not None:
            return seat.occupied
        return None

    def is_occupied(self, row: int, col: int) -> bool:
        seat = self._seats.get((row, col))
        if seat is not None:
            return seat.occupied
        return False

    def print(self) -> list[str]:
        return [
            "".join(
                RoomFactory.seat_char(self.get_seat(r, c))
                for c in range(self._col_count))
            for r in range(self._row_count)
        ]

    def count_seated(self):
        return count(self._seats.values(), lambda s: s.occupied)

    def simulate(self,
                 min_to_leave: int,
                 to_check: Optional[Iterable[Coord]] = None
                 ) -> tuple["Room", list[Coord]]:
        def check(curr: Seat) -> Seat:
            if curr.occupied:
                neighbors = sum(1 for r, c in curr.neighbors
                                if self.is_occupied(r, c))
                if neighbors >= min_to_leave:
                    changed.append(curr.pos)
                    return Seat(curr.pos, False, curr.neighbors)
            elif not any(self.is_occupied(*s) for s in curr.neighbors):
                changed.append(curr.pos)
                return Seat(curr.pos, True, curr.neighbors)
            return curr

        changed = list[Coord]()
        if to_check is None:
            to_check = list(self._seats.keys())

        next = self._seats.copy()
        next.update({k: check(self._seats[k]) for k in to_check})
        return Room(self._row_count, self._col_count, next), changed

    def get_connected(self, lst: Iterable[Coord]) -> Iterable[Coord]:
        result = set[Coord]()
        for item in lst:
            result.add(item)
            for n in self._seats[item].neighbors:
                result.add(n)
        return result

    def find_static(self, min_to_die: int) -> "Room":
        curr = self
        to_check: Optional[Iterable[Coord]] = None
        while True:
            next, changed = curr.simulate(min_to_die, to_check)
            if len(changed) == 0:
                return next
            to_check = next.get_connected(changed)
            curr = next


class RoomFactory:
    FLOOR = '.'
    EMPTY = 'L'
    SEATED = '#'

    @classmethod
    def seat_char(cls, occupied: Optional[bool]) -> str:
        if occupied is None:
            return RoomFactory.FLOOR
        elif occupied:
            return RoomFactory.SEATED
        return RoomFactory.EMPTY

    @classmethod
    def version_one(cls, rows: list[str]) -> Room:
        row_count = len(rows)
        col_count = len(rows[0])
        seats = Seats()
        for row in range(row_count):
            for col in range(col_count):
                if rows[row][col] != RoomFactory.FLOOR:
                    neighbors = []
                    for r in range(-1, 2):
                        for c in range(-1, 2):
                            curr_row = row + r
                            curr_col = col + c
                            if ((row != curr_row or col != curr_col)
                                    and curr_row in range(row_count)
                                    and curr_col in range(col_count)):
                                if rows[curr_row][
                                        curr_col] != RoomFactory.FLOOR:
                                    neighbors.append((curr_row, curr_col))
                    occupied = rows[row][col] == RoomFactory.SEATED
                    seats[(row, col)] = Seat((row, col), occupied, neighbors)
        return Room(row_count, col_count, seats)

    @classmethod
    def version_two(cls, rows: list[str]) -> Room:
        row_count = len(rows)
        col_count = len(rows[0])
        seats = Seats()
        for row in range(row_count):
            for col in range(col_count):
                if rows[row][col] != RoomFactory.FLOOR:
                    neighbors = []
                    for r in range(-1, 2):
                        for c in range(-1, 2):
                            if (r != 0 or c != 0):
                                curr_row = row + r
                                curr_col = col + c
                                while (curr_row in range(row_count)
                                       and curr_col in range(col_count)):
                                    if rows[curr_row][
                                            curr_col] != RoomFactory.FLOOR:
                                        neighbors.append((curr_row, curr_col))
                                        break
                                    curr_row += r
                                    curr_col += c
                    occupied = rows[row][col] == RoomFactory.SEATED
                    seats[(row, col)] = Seat((row, col), occupied, neighbors)
        return Room(row_count, col_count, seats)

    @classmethod
    def print_room(cls, room: Room) -> None:
        print("")
        for r in room.print():
            print(r)
        print("")
