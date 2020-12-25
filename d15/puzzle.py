def play_game(starting_numbers: list[int], elves_get_sick: int) -> int:
    elves_memory = dict[int, int]()
    for time, current_number in enumerate(starting_numbers):
        elves_memory[current_number] = time

    current_number = starting_numbers[-1]
    time_last_spoken = None

    game_starts = len(starting_numbers)
    for time in range(game_starts, elves_get_sick):
        if time_last_spoken is None:
            current_number = 0
        else:
            current_number = time - 1 - time_last_spoken

        time_last_spoken = elves_memory.get(current_number, None)
        elves_memory[current_number] = time

    return current_number
