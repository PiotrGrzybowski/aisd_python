from unittest import main, TestCase

from structures.queues import Stack


class TestStack(TestCase):
    def test_push(self):
        stack = Stack()

        stack.push(0)
        self.assertEqual(stack.top.value, 0)

        stack.push(1)
        self.assertEqual(stack.top.value, 1)
        self.assertEqual(stack.top.next.value, 0)

    def test_peek(self):
        stack = Stack()

        stack.push(0)
        self.assertEqual(stack.peek(), 0)

        stack.push(1)
        self.assertEqual(stack.peek(), 1)

    def test_pop(self):
        stack = Stack()

        stack.push(0)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.pop()

        self.assertEqual(stack.top.value, 2)


if __name__ == '__main__':
    main()
