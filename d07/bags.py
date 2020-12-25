import re
from typing import Iterable, Optional
from common.utils import some_filter

EntryDict = dict[str, int]
RuleEntry = tuple[str, EntryDict]


class Factory:
    # Intentionally ignore plural grammar
    _content = re.compile(r"^\s*(?P<num>\d+) (?P<color>.*) bags?\s*$")

    @staticmethod
    def _extract_contained(item: str) -> tuple[str, int]:
        match = Factory._content.match(item)
        if match is None:
            raise Exception("Not a valid rule", item)

        return match["color"], int(match["num"])

    _outer = re.compile(
        r"^(?P<color>.+) bags contain (no other bags|(?P<list>.+))\.$")

    @staticmethod
    def from_string(rule: str) -> Optional[RuleEntry]:
        match = Factory._outer.match(rule)
        if match is None:
            raise Exception("Not a valid rule", rule)

        if match["list"] is None:
            return None

        result = EntryDict(
            Factory._extract_contained(item)
            for item in match["list"].split(','))

        if len(result) > 0:
            return match["color"], result

    @staticmethod
    def from_rules(lines: list[str]) -> "BagRules":
        return BagRules(
            some_filter(Factory.from_string(line) for line in lines))


class BagRules:
    def __init__(self, rules: Iterable[RuleEntry]):
        self.bags = dict[str, EntryDict](rules)

    def count_outside_colors(self, to_find: str) -> int:
        processed = set[str]()
        still_to_check = {to_find}
        while still_to_check:
            bag = still_to_check.pop()

            containing = {k for k, v in self.bags.items() if bag in v.keys()}
            still_to_check |= containing

            still_to_check -= processed
            processed.add(bag)

        return len(processed) - 1

    def count_inside_bags(self, to_find: str) -> int:
        return sum(v * (self.count_inside_bags(k) + 1)
                   for k, v in self.bags.get(to_find, {}).items())
