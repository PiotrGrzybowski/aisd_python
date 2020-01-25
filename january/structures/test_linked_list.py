import unittest

from structures.lists import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_append(self):
        values = LinkedList()
        values.append(0)
        values.append(1)
        values.append(2)

        self.assertEqual(values.size, 3)
        self.assertEqual(values.head.value, 0)
        self.assertEqual(values.head.next.value, 1)
        self.assertEqual(values.head.next.next.value, 2)

    def test_extend(self):
        values = LinkedList()

        values.extend([0])
        self.assertEqual(values.size, 1)
        self.assertEqual(values.head.value, 0)

        values.extend([1, 2])
        self.assertEqual(values.size, 3)
        self.assertEqual(values.head.next.value, 1)
        self.assertEqual(values.head.next.next.value, 2)

    def test_insert(self):
        values = LinkedList()
        values.append('alice')
        values.insert(0, 'bob')
        values.insert(2, 'charlie')

        self.assertEqual(values.head.value, 'bob')
        self.assertEqual(values.head.next.value, 'alice')
        self.assertEqual(values.head.next.next.value, 'charlie')

    def test_remove(self):
        values = LinkedList()
        values.append(0)
        values.remove(0)

        self.assertEqual(values.size, 0)

        values.extend(['charlie', 'alice', 'bob', 'alice', 'alice'])
        values.remove('alice')

        self.assertEqual(values.size, 4)
        self.assertEqual(values.head.value, 'charlie')
        self.assertEqual(values.head.next.value, 'boc')
        self.assertEqual(values.head.next.next.value, 'alice')
        self.assertEqual(values.head.next.next.next.value, 'alice')

        values = LinkedList()
        values.append('ala')
        self.assertRaises(values.remove('charlie'), ValueError)

    def test_pop(self):
        values = LinkedList()
        values.extend(['charlie', 'alice', 'bob'])

        values.pop()
        self.assertEqual(values.size, 2)
        self.assertEqual(values.head.next.next, None)
        self.assertEqual(values.head.next.value, 'alice')
        self.assertEqual(values.head.value, 'charlie')

        values.pop(0)

        self.assertEqual(values.size, 1)
        self.assertEqual(values.head.value, 'alice')
        self.assertEqual(values.head.next, None)

    def test_count(self):
        values = LinkedList()
        values.extend(['charlie', 'alice', 'bob', 'alice', 'alice', 'charlie'])

        self.assertEqual(values.count('alice'), 3)
        self.assertEqual(values.count('piotr'), 0)
        self.assertEqual(values.count('charlie'), 2)

    def test_reverse(self):
        values = LinkedList()
        values.extend([1, 2, 3, 4])

        values.reverse()
        self.assertEqual(values.head.value, 4)
        self.assertEqual(values.head.next.value, 3)
        self.assertEqual(values.head.next.next.value, 2)
        self.assertEqual(values.head.next.next.next.value, 1)
        self.assertEqual(values.head.next.next.next.next, None)

        values = LinkedList()
        values.extend([1, 2, 3, 4, 5])

        values.reverse()
        self.assertEqual(values.head.value, 5)
        self.assertEqual(values.head.next.value, 4)
        self.assertEqual(values.head.next.next.value, 3)
        self.assertEqual(values.head.next.next.next.value, 2)
        self.assertEqual(values.head.next.next.next.next.value, 1)
        self.assertEqual(values.head.next.next.next.next.next, None)

    def test_len(self):
        values = LinkedList()
        values.append(0)
        values.append(1)
        values.append(2)

        self.assertEqual(len(values), 3)

        for _ in range(100):
            values.append(0)

        self.assertEqual(len(values), 103)

    def test_add(self):
        values_first = LinkedList()
        values_second = LinkedList()

        values_first.extend([0, 1])
        values_second.extend([2, 3])

        values = values_first + values_first

        self.assertEqual(values_first.size, 4)
        self.assertEqual(values.head.value, 0)
        self.assertEqual(values.head.next.value, 1)
        self.assertEqual(values.head.next.next.value, 2)
        self.assertEqual(values.head.next.next.next.value, 3)
        self.assertEqual(values.head.next.next.next.next, None)

        self.assertNotEqual(id(values_first), id(values))
        self.assertNotEqual(id(values_second), id(values))

    def test_in(self):
        values = LinkedList()
        values.append('charlie')

        self.assertTrue('charlie' in values)
        self.assertFalse('delta' in values)

    def test_if(self):
        values = LinkedList()

        self.assertFalse(True if values else False)

        values.append(0)
        self.assertTrue(True if values else False)

    def test_getitem(self):
        values = LinkedList()
        values.extend(['charlie', 'alice', 'bob', 'alice', 'alice', 'delta'])

        self.assertEqual(values[0], 'charlie')
        self.assertEqual(values[1], 'alice')
        self.assertEqual(values[-1], 'delta')
        self.assertEqual(values[-2], 'alice')

    def test_setitem(self):
        values = LinkedList()
        values.extend(['charlie', 'alice', 'bob', 'alice', 'alice', 'delta'])

        values[0] = 99
        values[3] = 100

        self.assertEqual(values.head.value[0], 99)
        self.assertEqual(values.head.next.next.next.value, 100)


if __name__ == '__main__':
    unittest.main()
