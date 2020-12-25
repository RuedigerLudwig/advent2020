import re
from typing import Optional

from common.utils import safe_get
from .token import Op, Operations, Token


class Tokenizer:
    @staticmethod
    def simple(line: str) -> Token:
        return Simple(line).token

    @staticmethod
    def advanced(line: str) -> Token:
        return Advanced(line).token

    @staticmethod
    def sum(tokens: list[Token]) -> int:
        return sum(t.get_value() for t in tokens)


class TokenException(Exception):
    pass


class Simple:
    pattern = re.compile(r"\s+|\d+|[+*]|\(|\)")

    def __init__(self, line: str):
        self.bits: list[str] = [
            p for p in Simple.pattern.findall(line.strip()) if p.strip() != ""
        ]
        if not self.bits:
            raise TokenException("Got nothing to parse")

        token, pos = self.parse_expression(0)
        if pos != len(self.bits):
            raise TokenException("Could not parse line")
        self.token = token

    def parse_item(self, pos: int) -> tuple[Token, int]:
        if self.bits[pos] == "(":
            item, pos = self.parse_expression(pos + 1)

            if safe_get(self.bits, pos, "") != ")":
                raise TokenException("Bracket not closed correctly")
        else:
            item = Token.from_int(self.bits[pos])

        return item, pos + 1

    def parse_expression(self, pos: int) -> tuple[Token, int]:
        token: Optional[Token] = None
        op: Optional[Op] = None
        while True:
            item, pos = self.parse_item(pos)
            token = Token.create(token, op, item)

            if (s := safe_get(self.bits, pos, "")) not in Operations:
                return token, pos

            op = s  # type: ignore
            pos += 1


class Advanced(Simple):
    def parse_sub_expression(self, pos: int) -> tuple[Token, int]:
        token: Optional[Token] = None
        while True:
            item, pos = self.parse_item(pos)
            token = Token.create(token, '+', item)

            if safe_get(self.bits, pos, "") != "+":
                return token, pos
            pos += 1

    def parse_expression(self, pos: int) -> tuple[Token, int]:
        token: Optional[Token] = None
        while True:
            item, pos = self.parse_sub_expression(pos)
            token = Token.create(token, '*', item)

            if safe_get(self.bits, pos, "") != "*":
                return token, pos
            pos += 1
