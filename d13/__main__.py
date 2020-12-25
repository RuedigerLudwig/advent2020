from common.utils import read_file
from .bus import BusFactory


def main() -> None:
    lines = read_file("d13/data/input.txt")
    earliest, busses = BusFactory.create_timetable(lines)
    bus, wait = BusFactory.get_best_bus(earliest, busses)
    print(f"Your have to wait {wait} minutes for bus {bus}")
    print(f"Your magic number is {bus * wait}")
    best_time = BusFactory.get_best_departure(busses)
    print(f"The best time is {best_time}")


if __name__ == "__main__":
    main()
