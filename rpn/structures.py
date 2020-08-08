from typing import TypeVar, List, Generic

T = TypeVar('T')


class EmptyQueueError(Exception):
    def __init__(self):
        super().__init__('You can not pop from empty Queue')


class Queue(Generic[T]):
    def __init__(self):
        self.values: List[T] = []

    def push(self, value: T):
        self.values.append(value)

    def pop(self) -> T:
        if self.values:
            return self.values.pop(0)
        else:
            raise EmptyQueueError()

    def front(self) -> T:
        return self.values[0]

    def __str__(self) -> str:
        return str(self.values)

    def __len__(self):
        return len(self.values)


class EmptyStackError(Exception):
    def __init__(self):
        super().__init__('You can not pop from empty Stack')


class Stack(Generic[T]):
    def __init__(self):
        self.values: List[T] = []

    def push(self, value: T):
        self.values.append(value)

    def pop(self) -> T:
        if self.values:
            return self.values.pop(-1)
        else:
            raise EmptyStackError()

    def front(self) -> T:
        return self.values[-1]

    def __str__(self) -> str:
        return str(self.values)

    def __len__(self):
        return len(self.values)
