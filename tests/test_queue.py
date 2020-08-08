from unittest import TestCase, main

from rpn.structures import Queue, EmptyQueueError


class TestQueue(TestCase):
    def test_push(self):
        queue = Queue[int]()

        queue.push(1)
        queue.push(2)
        queue.push(3)

        self.assertEqual(len(queue.values), 3)
        self.assertEqual(queue.values[0], 1)
        self.assertEqual(queue.values[1], 2)
        self.assertEqual(queue.values[2], 3)

    def test_pop(self):
        queue = Queue[int]()

        queue.push(1)
        queue.push(2)
        queue.push(3)

        popped = queue.pop()

        self.assertEqual(popped, 1)
        self.assertEqual(queue.values, [2, 3])

        queue.pop()
        queue.pop()

        self.assertRaises(EmptyQueueError, queue.pop)

    def test_front(self):
        queue = Queue[int]()

        queue.push(1)
        queue.push(2)
        queue.push(3)

        self.assertEqual(queue.front(), 1)

    def test_length(self):
        queue = Queue[int]()

        queue.push(1)
        queue.push(2)
        queue.push(3)

        self.assertEqual(len(queue), 3)


if __name__ == '__main__':
    main()
