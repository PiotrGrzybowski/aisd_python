from typing import Any


class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.array = self._make_empty_array(self.capacity)
        self.size = 0

    def append(self, value: Any) -> None:
        """
        Add value to the end of the list. Checks if capacity is enough.
        If not enough extend it.
        """
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        self.array[self.size] = value
        self.size += 1

    def count(self, value: Any) -> int:
        """
        Calculates how many occurrences of value in the list.
        """
        occurrences = 0

        for i in range(self.size):
            if self.array[i] == value:
                occurrences += 1

        return occurrences

    def pop(self, index=-1):
        if index >= self.size or index < -self.size:
            raise IndexError
        else:
            if index < 0:
                index = self.size + index
            element = self.array[index]
            for i in range(index, self.size):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            return element

    def clear(self):
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return f"[{', '.join([str(self.array[i]) for i in range(self.size)])}]"

    @staticmethod
    def _make_empty_array(capacity: int):
        return [None for _ in range(capacity)]

    def _resize(self, capacity: int):
        self.capacity = capacity
        new_array = self._make_empty_array(self.capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array

    def __contains__(self, value: Any) -> bool:
        for i in range(self.size):
            if self.array[i] == value:
                return True
        return False

    def __getitem__(self, index):
        if index > self.size or index < -self.size:
            raise IndexError()
        else:
            return self.array[:self.size][index]

    def __setitem__(self, index, value):
        if index > self.size or index < -self.size:
            raise IndexError()
        else:
            self.array[index] = value

    def __copy__(self):
        new_array = ArrayList()
        new_array.capacity = self.capacity
        new_array.size = self.size
        new_array.array = self._make_empty_array(new_array.capacity)

        for i in range(self.size):
            new_array[i] = self[i]

    def __bool__(self):
        return self.size > 0

if __name__ == '__main__':
    l = ArrayList()
    l.append(2)

    l[0] = 99
    print(l[0])
    print(l.pop())
    print(len(l))


