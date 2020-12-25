from .row import Row

MonsterInfo = tuple[set[tuple[int, int]], int, int]
Pos = tuple[int, int]


class Helper:
    @staticmethod
    def rotate(matrix: list[Row], turns: int, flip: bool) -> list[Row]:
        count = len(matrix)
        if turns == 1:
            if flip:
                return [
                    Row(matrix[count - c - 1][count - r - 1]
                        for c in range(count)) for r in range(count)
                ]
            return [
                Row(matrix[c][count - r - 1] for c in range(count))
                for r in range(count)
            ]
        elif turns == 2:
            if flip:
                return [
                    Row(matrix[count - r - 1][c] for c in range(count))
                    for r in range(count)
                ]
            return [
                Row(matrix[count - r - 1][count - c - 1] for c in range(count))
                for r in range(count)
            ]

        elif turns == 3:
            if flip:
                return [
                    Row(matrix[c][r] for c in range(count))
                    for r in range(count)
                ]
            return [
                Row(matrix[count - c - 1][r] for c in range(count))
                for r in range(count)
            ]
        elif flip:
            return [
                Row(matrix[r][count - c - 1] for c in range(count))
                for r in range(count)
            ]
        return matrix

    @staticmethod
    def convert_monster(monster: list[Row]) -> MonsterInfo:
        monster_height = len(monster)
        monster_width = len(monster[0])
        monster_bag = set[tuple[int, int]]()

        for r in range(monster_height):
            for c in range(monster_width):
                if monster[r][c]:
                    monster_bag.add((r, c))
        return monster_bag, monster_height, monster_width

    @staticmethod
    def check_for_monsters(image: list[Row],
                           monster: MonsterInfo) -> list[Pos]:
        def check_here(r: int, c: int) -> bool:
            for mr, mc in monster_bag:
                if not image[r + mr][c + mc]:
                    return False
            return True

        monster_bag, monster_height, monster_width = monster
        monsters_found = list[Pos]()

        for r in range(len(image) - monster_height):
            row = image[r]
            for c in range(len(row) - monster_width):
                if check_here(r, c):
                    monsters_found.append((r, c))
        return monsters_found
