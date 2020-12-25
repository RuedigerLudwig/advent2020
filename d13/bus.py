from typing import Optional
from math import ceil


class BusFactory:
    @staticmethod
    def get_schedule(time: str) -> Optional[int]:
        if time == "x":
            return None
        return int(time)

    @staticmethod
    def create_timetable(lines: list[str]) -> tuple[int, list[Optional[int]]]:
        earliest = int(lines[0])
        times = [BusFactory.get_schedule(t) for t in lines[1].split(",")]
        return earliest, times

    @staticmethod
    def get_best_bus(earliest: int,
                     times: list[Optional[int]]) -> tuple[int, int]:
        min_bus = 0
        min_wait = earliest * 2
        for bus in times:
            if bus is not None:
                wait = ceil(earliest / bus) * bus - earliest
                if wait < min_wait:
                    min_wait = wait
                    min_bus = bus
        return min_bus, min_wait

    @staticmethod
    def get_best_departure(busses: list[Optional[int]]) -> int:
        curr_value = 0
        curr_step = 1
        for delay, bus in enumerate(busses):
            if bus is not None:
                while (curr_value + delay) % bus != 0:
                    curr_value += curr_step
                curr_step *= bus
        return curr_value
