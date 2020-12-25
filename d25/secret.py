def part_one(card: int, door: int):
    subject = 7
    remainder = 20201227

    current_card = subject
    current_door = door
    while current_card != card:
        current_card = (current_card * subject) % remainder
        current_door = (current_door * door) % remainder

    return current_door
