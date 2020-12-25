from common.utils import read_file
from .room import RoomFactory


def main() -> None:
    seats = RoomFactory.version_one(read_file('d11/data/input.txt'))
    final = seats.find_static(4)
    print(f"In the end {final.count_occupied()} seats are taken")

    seats2 = RoomFactory.version_two(read_file('d11/data/input.txt'))
    final2 = seats2.find_static(5)
    print(f"In the real end {final2.count_occupied()} seats are taken")


if __name__ == "__main__":
    main()
