from structures.lists import ArrayList


class HashSet:
    def __init__(self, payload_factor=0.75, increase_factor=2, initial_buckets_size=4):
        self.payload_factor = payload_factor
        self.increase_factor = increase_factor
        self.initial_buckets_size = initial_buckets_size
        self.size = 0

        self.buckets = ArrayList()

    def add(self, value):
        pass

    def clear(self):
        pass

    def contains(self, value):
        pass

    def remove(self, item):
        pass

    def _increase_bucket_count(self, target_buckets_size):
        pass

    def buckets_str(self):
        pass

    def __str__(self) -> str:
        pass
