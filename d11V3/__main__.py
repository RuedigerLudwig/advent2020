from common.utils import read_file
from .room import RoomFactory


def main() -> None:
    seats = RoomFactory.version_one(read_file('d11/data/input.txt'))
    final = seats.find_static(4)
    print(f"Result 1: {final.count_seated()}")

    seats2 = RoomFactory.version_two(read_file('d11/data/input.txt'))
    final2 = seats2.find_static(5)
    print(f"Result 2: {final2.count_seated()}")


if __name__ == "__main__":
    main()
