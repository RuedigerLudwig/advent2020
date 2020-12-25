from abc import ABC, abstractmethod
from typing import Optional
import re

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
        return int(match["number"]), AltRule(match["number"], seq1, seq2)


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
    return {w for w in words if rules[0].matches(w, rules)}


def mingle_rules(rules: RuleDict) -> RuleDict:
    new_rules = rules.copy()
    new_rules[8] = RepeaterRule("8n", 8, [42])
    new_rules[11] = RepeaterRule("11n", 11, [42], [31])
    return new_rules


class Rule(ABC):
    @property
    def name(self) -> str:
        return self._name

    def __init__(self, name: str):
        self._name = name

    def matches(self, message: str, rules: RuleDict) -> bool:
        matched, _ = self.do_match(message, rules, 0, 0, True)
        return matched == len(message)

    @abstractmethod
    def do_match(self, message: str, rules: RuleDict, start_pos: int,
                 retake: int,
                 full_message: bool) -> tuple[Optional[int], bool]:
        pass


class CharRule(Rule):
    def __init__(self, name: str, char: str):
        super().__init__(name)
        self._char = char

    def __repr__(self):
        return f"CharRule({self.name}, {self._char})"

    def do_match(self, message: str, rules: RuleDict, start_pos: int,
                 retake: int,
                 full_message: bool) -> tuple[Optional[int], bool]:
        if retake == 0 and start_pos < len(message):
            if message[start_pos] == self._char:
                return start_pos + 1, True

        return None, True


class SequenceRule(Rule):
    def __init__(self, name: str, seq: list[int]):
        super().__init__(name)
        self._seq = seq

    def __repr__(self):
        return f"SequenceRule({self.name}, {self._seq})"

    @property
    def seq(self):
        return self._seq

    def do_match(self, message: str, rules: RuleDict, start_pos: int,
                 retake: int,
                 full_message: bool) -> tuple[Optional[int], bool]:
        def match_sub(rule_no: int, start_at: int) -> Optional[int]:
            rule = rules[self._seq[rule_no]]
            end_pos = None

            finished = False
            retake = 0

            while end_pos is None and not finished:
                is_last_rule = rule_no == len(self._seq) - 1
                end_pos, finished = rule.do_match(
                    message, rules, start_at, retake, is_last_rule
                    and full_message)

                if end_pos is not None:
                    if not is_last_rule:
                        end_pos = match_sub(rule_no + 1, end_pos)
                    elif full_message and end_pos != len(message):
                        end_pos = None
                retake += 1

            return end_pos

        if retake == 0:
            return match_sub(0, start_pos), True

        return None, True


class AltRule(Rule):
    def __init__(self, name: str, seq1: list[int], seq2: list[int]):
        super().__init__(name)

        self.rules = [
            SequenceRule(name + "/1", seq1),
            SequenceRule(name + "/2", seq2)
        ]

    def __repr__(self):
        return (f"AltRule({self.name}, "
                f"{self.rules[0].seq}, {self.rules[1].seq})")

    def do_match(self, message: str, rules: RuleDict, start_pos: int,
                 retake: int,
                 full_message: bool) -> tuple[Optional[int], bool]:
        if retake < len(self.rules):
            rule = self.rules[retake]
            end_pos, _ = rule.do_match(message, rules, start_pos, 0,
                                       full_message)
            return end_pos, retake + 1 >= len(self.rules)
        return None, True


class RepeaterRule(Rule):
    def __init__(self,
                 name: str,
                 orig: int,
                 first: list[int],
                 last: Optional[list[int]] = None):
        super().__init__(name)

        self.orig = orig
        self.first = SequenceRule(f"->{self.orig}", first)
        if last is not None:
            self.last = SequenceRule(f"{orig}<-", last)
        else:
            self.last = None

    def __repr__(self):
        if self.last is None:
            return f"RepeaterRule({self.name}, {self.first} *{self.orig}*)"
        else:
            return (f"RepeaterRule({self.name}, "
                    f"{self.first} *{self.orig}* {self.last.seq})")

    def do_match(self, message: str, rules: RuleDict, start_pos: int,
                 retake: int,
                 full_message: bool) -> tuple[Optional[int], bool]:
        def be_grabby(counter: int,
                      start_at: int) -> tuple[Optional[int], int, int]:
            end_pos, _ = self.first.do_match(message, rules, start_at, 0,
                                             False)

            if end_pos is not None:
                pass_result, retake_no, pass_runs = be_grabby(
                    counter + 1, end_pos)
                if retake_no == retake:
                    return end_pos, retake_no + 1, counter + 1
                else:
                    return pass_result, retake_no + 1, pass_runs
            else:
                return None, 0, 0

        end_pos, num_matches, num_runs = be_grabby(0, start_pos)

        if end_pos is not None:
            if self.last is not None:
                for run in range(num_runs):
                    is_last_run = run == num_runs - 1
                    end_pos, _ = self.last.do_match(
                        message, rules, end_pos, 0, full_message
                        and is_last_run)

                    if end_pos is None:
                        break

            return end_pos, retake + 1 >= num_matches

        return None, True
