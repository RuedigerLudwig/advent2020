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

    def run(self) -> tuple[int, bool]:
        acc = 0
        line = 0
        visited: set[int] = set()
        while line not in visited and line < len(self.code):
            visited.add(line)
            cmd, value = self.code[line]
            if cmd == "jmp":
                line += value
            else:
                line += 1
                if (cmd == "acc"):
                    acc += value

        return acc, line >= len(self.code)

    def run_fixed(self) -> int:
        last_change = -1
        while True:
            line = 0
            changed = False
            step = 0
            acc = 0
            visited = set[int]()
            while line not in visited and line < len(self.code):
                visited.add(line)
                step += 1
                cmd, value = self.code[line]
                if not changed and step > last_change and cmd != "acc":
                    cmd = "jmp" if cmd == "nop" else "nop"
                    last_change = step
                    changed = True

                if cmd == "jmp":
                    line += value
                else:
                    line += 1
                    if (cmd == "acc"):
                        acc += value

            if line >= len(self.code):
                return acc
