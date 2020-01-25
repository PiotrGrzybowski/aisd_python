from unittest import main, TestCase

from structures.queues import FifoQueue


class TestStack(TestCase):
    def test_push(self):
        queue = FifoQueue()

        queue.push(0)
        self.assertEqual(queue.front.value, 0)
        self.assertEqual(queue.end.value, 0)

        queue.push(1)
        self.assertEqual(queue.front.value, 0)
        self.assertEqual(queue.front.next.value, 1)
        self.assertEqual(queue.end.value, 1)

    def test_peek(self):
        queue = FifoQueue()

        queue.push(0)
        self.assertEqual(queue.peek(), 0)

        queue.push(1)
        self.assertEqual(queue.peek(), 1)

    def test_pop(self):
        queue = FifoQueue()

        queue.push(0)
        queue.push(1)
        queue.push(2)
        value = queue.pop()

        self.assertEqual(value, 0)
        self.assertEqual(queue.front.value, 1)

    def test_len(self):
        queue = FifoQueue()

        queue.push(0)
        queue.push(1)
        queue.push(2)

        self.assertEqual(len(queue), 3)


if __name__ == '__main__':
    main()
