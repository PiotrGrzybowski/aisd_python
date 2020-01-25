class HashSet:
    def __init__(self, payload_factor=0.75, increase_factor=2, initial_buckets_size=4):
        self.payload_factor = payload_factor
        self.increase_factor = increase_factor
        self.initial_buckets_size = initial_buckets_size
        self.size = 0

        self.buckets = [[] for _ in range(self.initial_buckets_size)]

    def add(self, value):
        if not self.contains(value):
            if self.size / len(self.buckets) >= self.payload_factor:
                self._increase_bucket_count(len(self.buckets) * self.increase_factor)
            value_hash = hash(value)
            bucket_index = value_hash % len(self.buckets)
            self.buckets[bucket_index].append(value)
            self.size += 1

    def clear(self):
        for bucket in self.buckets:
            bucket.clear()
        self.size = 0

    def contains(self, value):
        item_bucket_index = hash(value) % len(self.buckets)
        return value in self.buckets[item_bucket_index]

    def remove(self, item):
        item_bucket = hash(item) % len(self.buckets)
        bucket = self.buckets[item_bucket]
        old_bucket_elements = len(bucket)
        bucket.remove(item)

        self.size -= (old_bucket_elements - len(bucket))

    def _increase_bucket_count(self, target_buckets_size):
        new_buckets = [[] for _ in range(target_buckets_size)]
        for old_bucket in self.buckets:
            for element in old_bucket:
                new_bucket_index = hash(element) % len(new_buckets)
                new_buckets[new_bucket_index].append(element)
        self.buckets = new_buckets

    def buckets_str(self):
        return '\n'.join([f'{i:2}: {str(bucket)}' for i, bucket in enumerate(self.buckets)])

    def __str__(self) -> str:
        elements = ', '.join([str(element) for bucket in self.buckets for element in bucket])
        return f'{{{elements}}}'
