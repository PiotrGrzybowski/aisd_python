from typing import Union

from rpn.token import Token


class Number(Token):
    def __init__(self, text: str):
        super().__init__(text)

        self.value = float(self.text)

    def __str__(self) -> str:
        return self.text
