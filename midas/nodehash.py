import numpy as np


class Nodehash:
    def __init__(self, r, b):
        self.num_rows = r
        self.num_buckets = b
        self.hash_a = np.random.randint(low=1, high=b, size=r)
        self.hash_b = np.random.randint(low=0, high=b, size=r)
        self.count = np.zeros((self.num_rows, self.num_buckets))

    def hash(self, a, i):
        resid = (a * self.hash_a[i] + self.hash_b[i]) % self.num_buckets
        return resid + (self.num_buckets if (resid < 0) else 0)

    def insert(self, a, weight):
        for i in range(self.num_rows):
            bucket = self.hash(a, i)
            self.count[i][bucket] += weight

    def get_count(self, a):
        bucket = self.hash(a, 0)
        min_count = self.count[0][bucket]
        for i in range(1, self.num_rows):
            bucket = self.hash(a, i)
            min_count = min(min_count, self.count[i][bucket])

        return min_count

    def clear(self):
        self.count = np.zeros((self.num_rows, self.num_buckets))

    def lower(self, factor):
        self.count = self.count * factor
