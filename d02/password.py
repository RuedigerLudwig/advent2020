import re


class Password:
    def __init__(self, letter: str, fst: int, snd: int, password: str):
        self.letter = letter
        self.fst = fst
        self.snd = snd
        self.password = password

    def is_valid_sled(self) -> bool:
        return self.fst <= self.password.count(self.letter) <= self.snd

    def is_valid_tobbogan(self) -> bool:
        return ((self.password[self.fst - 1] == self.letter) ^
                (self.password[self.snd - 1] == self.letter))


class Factory:
    _parser = re.compile(r"^(?P<fst>\d+)-(?P<snd>\d+) "
                         r"(?P<letter>[a-z]): (?P<password>.*)$")

    @staticmethod
    def fromString(string: str) -> Password:
        match = Factory._parser.match(string)
        if match is None:
            raise Exception(f"Not a valid password: {str}")

        return Password(match["letter"], int(match["fst"]), int(match["snd"]),
                        match["password"])
