import unittest

from structures.lists import ArrayList


class TestArrayList(unittest.TestCase):
    def test_append(self):
        values = ArrayList()
        values.append(0)
        values.append(1)
        values.append(2)

        self.assertEqual(values.size, 3)
        self.assertEqual(values.array[0], 0)
        self.assertEqual(values.array[1], 1)
        self.assertEqual(values.array[2], 2)

    def test_extend(self):
        values = ArrayList()

        values.extend([0])
        self.assertEqual(values.size, 1)
        self.assertEqual(values.array[0], 0)

        values.extend([1, 2])
        self.assertEqual(values.size, 3)
        self.assertEqual(values.array[0], 0)
        self.assertEqual(values.array[2], 2)

        values.extend([3, 4, 5])
        self.assertEqual(values.size, 6)
        self.assertEqual(values.array[0], 0)
        self.assertEqual(values.array[2], 2)
        self.assertEqual(values.array[4], 4)

    def test_insert(self):
        values = ArrayList()
        values.append('alice')
        values.insert(0, 'bob')
        values.insert(2, 'charlie')

        self.assertEqual(values.array[0], 'bob')
        self.assertEqual(values.array[1], 'alice')
        self.assertEqual(values.array[2], 'charlie')

    def test_remove(self):
        values = ArrayList()
        values.append(0)
        values.remove(0)

        self.assertEqual(values.size, 0)

        values.extend(['charlie', 'alice', 'bob', 'alice', 'alice'])
        values.remove('alice')

        self.assertEqual(values.size, 4)
        self.assertEqual(values.array[0], 'charlie')
        self.assertEqual(values.array[1], 'bob')
        self.assertEqual(values.array[2], 'alice')
        self.assertEqual(values.array[3], 'alice')

        values = ArrayList()
        values.append('ala')
        self.assertRaises(values.remove('charlie'), ValueError)

    def test_pop(self):
        values = ArrayList()
        values.extend(['charlie', 'alice', 'bob', 'alice', 'alice'])

        values.pop()
        self.assertEqual(values.size, 4)
        self.assertEqual(values.array, ['charlie', 'alice', 'bob', 'alice'])

        values.pop(1)
        values.pop(1)

        self.assertEqual(values.size, 2)
        self.assertEqual(values.array, ['charlie', 'alice'])

    def test_clear(self):
        values = ArrayList()
        values.extend(['charlie', 'alice', 'bob', 'alice', 'alice'])

        values.clear()
        self.assertEqual(values.size, 0)

    def test_count(self):
        values = ArrayList()
        values.extend(['charlie', 'alice', 'bob', 'alice', 'alice', 'charlie'])

        self.assertEqual(values.count('alice'), 3)
        self.assertEqual(values.count('piotr'), 0)
        self.assertEqual(values.count('charlie'), 2)

    def test_reverse(self):
        values = ArrayList()
        values.extend([1, 2, 3, 4])

        values.reverse()
        self.assertEqual(values.array, [4, 3, 2, 1])

        values = ArrayList()
        values.extend([1, 2, 3, 4, 5])

        values.reverse()
        self.assertEqual(values.array, [5, 4, 3, 2, 1])

    def test_len(self):
        values = ArrayList()
        values.append(0)
        values.append(1)
        values.append(2)

        self.assertEqual(len(values), 3)

        for _ in range(100):
            values.append(0)

        self.assertEqual(len(values), 103)

    def test_add(self):
        values_first = ArrayList()
        values_second = ArrayList()

        values_first.extend([0, 1])
        values_second.extend([2, 3])

        values = values_first + values_first

        self.assertEqual(values_first.size, 4)
        self.assertEqual(values.array[0], 0)
        self.assertEqual(values.array[1], 1)
        self.assertEqual(values.array[2], 2)
        self.assertEqual(values.array[3], 3)

        self.assertNotEqual(id(values_first), id(values))
        self.assertNotEqual(id(values_second), id(values))

    def test_in(self):
        values = ArrayList()
        values.append('charlie')

        self.assertTrue('charlie' in values)
        self.assertFalse('delta' in values)

    def test_if(self):
        values = ArrayList()
        result = None

        self.assertFalse(True if values else False)

        values.append(0)
        self.assertTrue(True if values else False)

    def test_getitem(self):
        values = ArrayList()
        values.extend(['charlie', 'alice', 'bob', 'alice', 'alice', 'delta'])

        self.assertEqual(values[0], 'charlie')
        self.assertEqual(values[1], 'alice')
        self.assertEqual(values[-1], 'delta')
        self.assertEqual(values[-2], 'alice')

    def test_setitem(self):
        values = ArrayList()
        values.extend(['charlie', 'alice', 'bob', 'alice', 'alice', 'delta'])

        values[0] = 99
        values[3] = 100

        self.assertEqual(values.array[0], 99)
        self.assertEqual(values.array[3], 100)


if __name__ == '__main__':
    unittest.main()