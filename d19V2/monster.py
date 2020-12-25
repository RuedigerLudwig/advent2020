from abc import ABC, abstractmethod
from typing import Iterable, Optional
import re
import regex  # type: ignore

char_pattern = re.compile(r'^(?P<number>\d+): "(?P<char>.)"$')
sequence_pattern = re.compile(r"(?P<number>\d+): (?P<seq>(\d+\s?)+)$")
alt_pattern = re.compile(r"(?P<number>\d+): "
                         r"(?P<seq1>(\d+\s?)+)\| (?P<seq2>(\d+\s?)+)$")

RuleDict = dict[int, "Rule"]


def parse(line: str) -> Optional[tuple[int, "Rule"]]:
    def int_list(lst: str) -> list[int]:
        return [int(i) for i in lst.strip().split(" ")]

    if line == "":
        return None

    if match := char_pattern.match(line):
        return int(match["number"]), CharRule(match["number"], match["char"])

    if match := sequence_pattern.match(line):
        seq = int_list(match["seq"])
        return int(match["number"]), SequenceRule(match["number"], seq)

    if match := alt_pattern.match(line):
        seq1 = int_list(match["seq1"])
        seq2 = int_list(match["seq2"])
        return int(match["number"]), AltRule(match["number"], (seq1, seq2))


def parse_lines(lines: list[str]) -> tuple[RuleDict, list[str]]:
    rules = RuleDict()
    it = iter(lines)
    try:
        while result := parse(next(it).strip()):
            rules[result[0]] = result[1]
    except StopIteration:
        raise Exception

    words = list(it)
    return rules, words


def count_matches(words: list[str], rules: RuleDict) -> int:
    return len(get_matches(words, rules))


def get_matches(words: list[str], rules: RuleDict) -> set[str]:
    reg = "^" + rules[0].get_regexp(rules) + "$"
    return {
        message
        for message in words
        if regex.match(reg, message) is not None  # type: ignore
    }


def mingle_rules(rules: RuleDict) -> RuleDict:
    new_rules = rules.copy()
    new_rules[8] = RepeaterRule("n8", [42])
    new_rules[11] = RepeaterRule("n11", [42], [31])
    return new_rules


class Rule(ABC):
    @property
    def name(self) -> str:
        return self._name

    def __init__(self, name: str):
        self._name = name

    def matches(self, message: str, rules: RuleDict) -> bool:
        reg = "^" + self.get_regexp(rules) + "$"
        return regex.match(reg, message) is not None  # type: ignore

    @abstractmethod
    def get_regexp(self, rules: RuleDict) -> str:
        pass


class CharRule(Rule):
    def __init__(self, name: str, char: str):
        super().__init__(name)
        self._char = char

    def __repr__(self):
        return f"CharRule({self.name}, {self._char})"

    def get_regexp(self, rules: RuleDict) -> str:
        return self._char


class SequenceRule(Rule):
    def __init__(self, name: str, seq: list[int]):
        super().__init__(name)
        self._seq = seq

    def __repr__(self):
        return f"SequenceRule({self.name}, {self._seq})"

    @property
    def seq(self):
        return self._seq

    def get_regexp(self, rules: RuleDict) -> str:
        return "".join(rules[rule].get_regexp(rules) for rule in self._seq)


class AltRule(Rule):
    def __init__(self, name: str, sequence: Iterable[list[int]]):
        super().__init__(name)

        self.rules = [
            SequenceRule(f"{name}/{pos}", seq)
            for pos, seq in enumerate(sequence)
        ]

    def __repr__(self):
        return (f"AltRule({self.name}, "
                f"{', '.join(str(rule.seq) for rule in self.rules)})")

    def get_regexp(self, rules: RuleDict) -> str:
        return "(" + "|".join(rule.get_regexp(rules)
                              for rule in self.rules) + ")"


class RepeaterRule(Rule):
    def __init__(self,
                 name: str,
                 first: list[int],
                 last: Optional[list[int]] = None):
        super().__init__(name)

        self.first = SequenceRule(f"->{name}", first)
        if last is not None:
            self.last = SequenceRule(f"{name}<-", last)
        else:
            self.last = None

    def __repr__(self):
        if self.last is None:
            return f"RepeaterRule({self.name}, {self.first} *{self.name}*)"
        else:
            return (f"RepeaterRule({self.name}, "
                    f"{self.first} *{self.name}* {self.last.seq})")

    def get_regexp(self, rules: RuleDict) -> str:
        if self.last is None:
            return "(" + self.first.get_regexp(rules) + ")+"
        else:
            result = (f"(?P<{self.name}>" + self.first.get_regexp(rules) +
                      f"(?P&{self.name})?" + self.last.get_regexp(rules) + ")")
            return result
