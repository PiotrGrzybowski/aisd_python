class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = Node(value)

    def __str__(self):
        if self.head is None:
            return ''
        else:
            values = []
            current = self.head
            while current is not None:
                values.append(str(current.value))
                current = current.next

            return f"{' -> '.join(values)}"


def sum_linked_list(linked_list: LinkedList) -> int:
    result = 0
    current = linked_list.head
    while current is not None:
        result += current.value
        current = current.next
    return result


if __name__ == '__main__':
    l = LinkedList()
    l.append(5)
    l.append(6)
    l.append(0)
    print(l)

