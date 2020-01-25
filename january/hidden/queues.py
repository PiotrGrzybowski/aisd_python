from abc import ABC, abstractmethod


class Queue(ABC):
    def __init__(self):
        self.size = 0

    @abstractmethod
    def push(self, x):
        """Add an item at the beginning of the queue."""
        pass

    @abstractmethod
    def pop(self):
        """Remove an item from queue."""
        pass

    @abstractmethod
    def peek(self):
        """Get element from top of the queue but don't remove"""
        pass

    def __len__(self):
        """Return number of elements in the queue."""
        pass


class Stack(Queue):
    def __init__(self):
        super().__init__()
        self.top = None

    def push(self, x):
        """Add an item onto top of the stack."""
        pass

    def pop(self):
        """Remove an item from top of the stack."""
        pass

    def peek(self):
        """Get element from top of the stack but don't remove"""
        pass

    def __len__(self):
        """Return number of elements on the stack."""
        pass


class FifoQueue:
    def __init__(self):
        self.front = None
        self.end = None

    def push(self, x):
        """Add an item at the end of the queue."""
        pass

    def pop(self):
        """Remove an item from the end of the queue."""
        pass

    def peek(self):
        """Get element at the front in the queue."""
        pass

    def __len__(self):
        """Return number of elements in the queue."""
        pass
