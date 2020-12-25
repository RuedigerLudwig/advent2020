from common.utils import read_file
from .password import Factory


def main() -> None:
    passwords = read_file("d02/data/input.txt", Factory.fromString)

    valid_passwords_sled = [p for p in passwords if p.is_valid_sled()]
    print(f"Result 1 Sled:     {len(valid_passwords_sled)}")

    valid_passwords_toboggan = [p for p in passwords if p.is_valid_tobbogan()]
    print(f"Result 2 Toboggan: {len(valid_passwords_toboggan)}")


if __name__ == "__main__":
    main()
