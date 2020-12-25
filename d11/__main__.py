from common.utils import read_file
from .room import Factory


def main() -> None:
    seats = Factory.from_lines(read_file("d11/data/input.txt"))

    final = seats.simulate_to_fixed()
    print(f"Result 1: {final.count_seats()}")

    final2 = seats.simulate_to_fixed2()
    print(f"Result 2: {final2.count_seats()}")


if __name__ == "__main__":
    main()
