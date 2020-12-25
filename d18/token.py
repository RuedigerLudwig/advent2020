from abc import ABC, abstractmethod
from typing import Literal, Optional, Union, overload

Operations = ("*", "+")

Op = Literal["*", "+"]
TokenTuple = Union[int, tuple[Op, "TokenTuple", "TokenTuple"]]


class Token(ABC):
    @abstractmethod
    def get_value(self) -> int:
        pass

    def __str__(self) -> str:
        return str(self.get_value())

    def __eq__(self, other: "Token") -> bool:
        try:
            return self.get_value() == other.get_value()
        except Exception:
            raise NotImplementedError

    @abstractmethod
    def as_tuple(self) -> TokenTuple:
        pass

    @overload
    @staticmethod
    def from_int(val: int) -> "Token":
        ...

    @overload
    @staticmethod
    def from_int(val: str) -> "Token":
        ...

    @staticmethod
    def from_int(val: Union[str, int]) -> "Token":
        if isinstance(val, int):
            return IntToken(val)

        return IntToken(int(val))

    @staticmethod
    def create(first: Optional["Token"], op: Optional[Op],
               second: "Token") -> "Token":
        if first is None:
            return second
        elif op == "+":
            return AddToken(first, second)
        else:
            return MulToken(first, second)


class IntToken(Token):
    def __init__(self, value: int):
        self.value = value

    def get_value(self) -> int:
        return self.value

    def as_tuple(self) -> TokenTuple:
        return self.value


class AddToken(Token):
    def __init__(self, first: Token, second: Token):
        self.first = first
        self.second = second

    def get_value(self) -> int:
        return self.first.get_value() + self.second.get_value()

    def as_tuple(self) -> TokenTuple:
        return "+", self.first.as_tuple(), self.second.as_tuple()


class MulToken(Token):
    def __init__(self, first: Token, second: Token):
        self.first = first
        self.second = second

    def get_value(self) -> int:
        return self.first.get_value() * self.second.get_value()

    def as_tuple(self) -> TokenTuple:
        return "*", self.first.as_tuple(), self.second.as_tuple()
