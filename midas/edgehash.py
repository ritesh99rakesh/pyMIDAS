import numpy as np


class Edgehash:
    def __init__(self, r, b, m0):
        self.num_rows = r
        self.num_buckets = b
        self.m = m0
        self.hash_a = np.random.randint(low=1, high=b, size=r)
        self.hash_b = np.random.randint(low=0, high=b, size=r)
        self.count = np.zeros((self.num_rows, self.num_buckets))

    def hash(self, a, b, i):
        resid = ((a + self.m * b) * self.hash_a[i] + self.hash_b[i]) % self.num_buckets
        return resid + (self.num_buckets if (resid < 0) else 0)

    def insert(self, a, b, weight):
        for i in range(self.num_rows):
            bucket = self.hash(a, b, i)
            self.count[i][bucket] += weight

    def get_count(self, a, b):
        bucket = self.hash(a, b, 0)
        min_count = self.count[0][bucket]
        for i in range(1, self.num_rows):
            bucket = self.hash(a, b, i)
            min_count = min(min_count, self.count[i][bucket])

        return min_count

    def clear(self):
        self.count = np.zeros((self.num_rows, self.num_buckets))

    def lower(self, factor):
        self.count = self.count * factor
