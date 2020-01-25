from unittest import TestCase, main

from structures.hash_tables import HashSet


class TestHashSet(TestCase):
    def test_add(self):
        s = HashSet()
        s.add(5)
        s.add(5)
        s.add(4)
        s.add(1)
        s.add(9)
        print(s.buckets_str())
        print(s)


if __name__ == '__main__':
    main()
