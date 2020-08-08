from typing import Dict

from rpn.operators import Operator
from rpn.structures import Queue, Stack
from rpn.token import Token


class ExpressionParser:
    def __init__(self, operators: Dict[str, Operator]):
        self.operators = operators
        self.infix_expression = None
        self.output_queue = Queue[Token]()
        self.tokens_stack = Stack[Token]()
        self.index = 0
