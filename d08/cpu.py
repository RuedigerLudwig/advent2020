import re

pattern = re.compile(r"^(?P<inst>nop|acc|jmp) (?P<value>[-+]\d+)$")


class Factory:
    @staticmethod
    def from_string(line: str) -> tuple[str, int]:
        match = pattern.match(line)
        if match is None:
            raise Exception(f"Not a valid instruction: {line}")

        return match["inst"], int(match["value"])

    @staticmethod
    def get_code(lines: list[str]) -> "Code":
        return Code([Factory.from_string(line) for line in lines])


class Code:
    def __init__(self, code: list[tuple[str, int]]):
        self.code = code

    @staticmethod
    def _run(code: list[tuple[str, int]]) -> tuple[int, bool]:
        acc = 0
        line = 0
        visited: set[int] = set()
        while line not in visited and line < len(code):
            visited.add(line)
            cmd, value = code[line]
            if cmd == "jmp":
                line += value
            else:
                line += 1
                if (cmd == "acc"):
                    acc += value
        return acc, line >= len(code)

    def run(self) -> tuple[int, bool]:
        return Code._run(self.code)

    def run_fixed(self) -> int:
        code = self.code

        changed_line = 0
        while True:
            while changed_line < len(code) and code[changed_line][0] == "acc":
                changed_line += 1

            if changed_line >= len(code):
                raise Exception("Can't fix this")

            fixed_code = code.copy()
            fixed_cmd = {"jmp": "nop", "nop": "jmp"}[code[changed_line][0]]
            fixed_code[changed_line] = (fixed_cmd, fixed_code[changed_line][1])

            acc, finished = Code._run(fixed_code)
            if finished:
                return acc
            changed_line += 1
