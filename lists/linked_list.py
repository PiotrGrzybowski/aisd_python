from typing import Any
from dataclasses import dataclass


@dataclass
class Node:
    value: Any
    next_node: 'Node' = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, elem):
        if self.head is None:
            self.head = Node(elem)
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node

            current.next_node = Node(elem)

    def prepend(self, elem):
        if self.head is None:
            self.head = Node(elem)
        else:
            new_node = Node(elem, self.head)
            self.head = new_node

    def __len__(self):
        next_node = self.head
        lenght = 0
        while next_node is not None:
            lenght += 1
            next_node = next_node.next_node

        return lenght

    def __getitem__(self, index):
        node = self.head
        while node is not None:
            if index == 0:
                return node.value
            index -= 1
            node = node.next_node
        raise IndexError()

    def __setitem__(self, index, value):
        if self.head is Node:
            raise IndexError()

        counter = 0
        current = self.head
        while counter < index and current.next_node is not None:
            current = current.next_node
            counter += 1

        if counter == index:
            current.value = value
        else:
            raise IndexError()


empty = LinkedList()
# print(empty.head)
empty.append(1)
# print(empty.head)
empty.append(2)
# print(empty.head)

for k in empty:
    print(k)

empty[1] = 12
empty[0] = 12
for k in empty:
    print(k)
# print(len(empty))
# print(empty[0])
# print(empty[1])
# print(empty[2])
# print(empty[3])
# print(empty[4])
