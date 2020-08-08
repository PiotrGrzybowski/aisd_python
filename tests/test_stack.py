from unittest import TestCase, main

from rpn.structures import Stack, EmptyStackError


class TestStack(TestCase):
    def test_push(self):
        stack = Stack[int]()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(len(stack.values), 3)
        self.assertEqual(stack.values[0], 1)
        self.assertEqual(stack.values[1], 2)
        self.assertEqual(stack.values[2], 3)

    def test_pop(self):
        stack = Stack[int]()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        popped = stack.pop()

        self.assertEqual(popped, 3)
        self.assertEqual(stack.values, [1, 2])

        stack.pop()
        stack.pop()

        self.assertRaises(EmptyStackError, stack.pop)

    def test_front(self):
        stack = Stack[int]()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.front(), 3)

    def test_length(self):
        stack = Stack[int]()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(len(stack), 3)


if __name__ == '__main__':
    main()
