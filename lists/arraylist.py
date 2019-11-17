from abc import ABC, abstractmethod
from copy import copy
from typing import Any


class IndexOutOfBoundException(Exception):
    pass


class List(ABC):
    @abstractmethod
    def append(self, element: Any):
        pass

#
# class ArrayListIterator:
#     def __init__(self, array_list: 'ArrayList'):
#         self.array_list = array_list
#         self.index = 0
#
#     def __next__(self):
#         if self.index < len(self.array_list):
#             result = self.array_list[self.index]
#             self.index += 1
#             return result
#
#         raise StopIteration


class ArrayList(List):
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.array = self._make_array(self.capacity)

    def append(self, element: Any):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.size] = element
        self.size += 1

    def pop(self, index=None):
        if index is None:
            index = self.size - 1

        self._check_out_of_bounds(index)
        element = self.array[index]

        if index + 1 < self.size:
            self._delete_element(index)

        self.size -= 1

        return element

    def clear(self):
        self.array = self._make_array(self.capacity)

    def count(self, value: Any):
        result = 0
        for elem in self.array:
            if elem == value:
                result += 1

        return result

    def reverse(self):
        for i in range(self.size // 2):
            temp = self.array[i]
            self.array[i] = self.array[self.size - 1 - i]
            self.array[self.size - 1 - i] = temp

    def __contains__(self, value: Any):
        for elem in self.array:
            if elem == value:
                return True

        return False

    def __bool__(self):
        return self.size < 1

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index > self.size - 1:
            raise IndexError()

        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def __str__(self):
        return f"[{','.join([str(self.array[i]) for i in range(self.size)])}]"

    # def __iter__(self):
    #     return ArrayListIterator(self)

    def __copy__(self):
        new_list = ArrayList()
        new_list.capacity = self.capacity
        new_list.array = self._make_array(new_list.capacity)
        new_list.size = self.size

        for i in range(self.size):
            new_list[i] = self.array[i]

        return new_list

    def _resize(self, capacity: int):
        new_array = self._make_array(capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = capacity

    def _check_out_of_bounds(self, index: int):
        if index >= self.size:
            raise IndexOutOfBoundException()

    def _delete_element(self, index):
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

    @staticmethod
    def _make_array(capacity: int):
        return [None for _ in range(capacity)]




if __name__ == '__main__':
    a = ArrayList()
    a.append(1)
    a.append(2)
    a.append(3)
    a.append(4)
    a.append(5)
    a.reverse()
    for x in a:
        print(x)
    print(copy(a))

    if a:
        print(True)
    # [].