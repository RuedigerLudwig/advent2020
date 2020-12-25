from common.utils import read_file
from .storm import StormFactory


def main() -> None:
    actions = read_file('d12/data/input.txt', StormFactory.from_string)
    result = StormFactory.get_distance(actions)
    print(f"Result 1: {result}")

    result2 = StormFactory.get_waypoint_distance(actions)
    print(f"Result 2: {result2}")


if __name__ == "__main__":
    main()
