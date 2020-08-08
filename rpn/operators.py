from abc import abstractmethod
from enum import Enum

from rpn.token import Token


class Associativity(Enum):
    LEFT: int = 1
    RIGHT: int = 2


class Operator(Token):
    def __init__(self, text: str, precedence: int, associativity: Associativity):
        super().__init__(text)
        self.precedence = precedence
        self.associativity = associativity

    @abstractmethod
    def evaluate(self, *args):
        pass


class Addition(Operator):
    def evaluate(self, number_1: float, number_2: float):
        return number_1 + number_2

    def __str__(self) -> str:
        return '+'
