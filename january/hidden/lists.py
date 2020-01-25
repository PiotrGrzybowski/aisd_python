from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


class IndexOutOfBoundException(Exception):
    pass


class List(ABC):
    @abstractmethod
    def append(self, x):
        """Add an item to the end of the list."""
        pass

    @abstractmethod
    def extend(self, iterable):
        """Extend the list by appending all the items from the iterable."""
        pass

    @abstractmethod
    def insert(self, i, x):
        """
        Insert an item at a given position. The first argument is the index of the element before which to insert,
        so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x)
        """
        pass

    @abstractmethod
    def remove(self, x):
        """
        Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
        """

    @abstractmethod
    def pop(self, i):
        """
        Remove the item at the given position in the list, and return it. If no index is specified, a.pop()
        removes and returns the last item in the list.
        """
        pass

    @abstractmethod
    def clear(self):
        """Remove all items from the list."""
        pass

    @abstractmethod
    def count(self, x):
        """Return the number of times x appears in the list."""
        pass

    @abstractmethod
    def reverse(self):
        """Reverse the elements of the list in place."""
        pass

    @abstractmethod
    def __add__(self, other):
        """Creates new list from self and the other"""
        pass

    @abstractmethod
    def __bool__(self):
        """Return True if there is at least one element in the list."""
        pass

    @abstractmethod
    def __contains__(self, x):
        """Return True if list contain x."""
        pass

    @abstractmethod
    def __getitem__(self, i):
        """Return i-th element from the list."""
        pass

    @abstractmethod
    def __len__(self):
        """Return number of elements in the list."""
        pass

    @abstractmethod
    def __setitem__(self, i, x):
        """Assign new value x at the i-th index."""
        pass

    @abstractmethod
    def __str__(self):
        """Return text representation of the list."""
        pass


class ArrayList(List):
    def __init__(self, elements=None, capacity=4):
        self.size = 0
        self.capacity = capacity
        self.array = []

        if elements:
            self.extend(elements)

    def append(self, x):
        pass

    def extend(self, iterable):
        pass

    def insert(self, i, x):
        pass

    def remove(self, x):
        pass

    def pop(self, i=None):
        pass

    def clear(self):
        pass

    def count(self, x):
        pass

    def reverse(self):
        pass

    def __add__(self, other):
        pass

    def __bool__(self):
        pass

    def __contains__(self, x):
        pass

    def __getitem__(self, i):
        pass

    def __len__(self):
        pass

    def __setitem__(self, i, x):
        pass

    def __str__(self):
        pass


@dataclass
class Node:
    value: Any
    next_node: 'Node' = None


class LinkedList(List):
    def __init__(self, elements=None):
        self.size = 0
        self.head = None

        if elements:
            self.extend(elements)

    def append(self, x):
        pass

    def extend(self, iterable):
        pass

    def insert(self, i, x):
        pass

    def remove(self, x):
        pass

    def pop(self, i=None):
        pass

    def clear(self):
        pass

    def count(self, x):
        pass

    def reverse(self):
        pass

    def __add__(self, other):
        pass

    def __bool__(self):
        pass

    def __contains__(self, x):
        pass

    def __copy__(self):
        pass

    def __getitem__(self, i):
        pass

    def __len__(self):
        pass

    def __setitem__(self, i, x):
        pass

    def __str__(self):
        pass


if __name__ == '__main__':
    l: list = []
    k = ArrayList()
    k = LinkedList()
