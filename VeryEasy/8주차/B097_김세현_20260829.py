class MyHashMap:
    def __init__(self):
        self.bucket_count = 769
        self.buckets = [[] for _ in range(self.bucket_count)]

    def _bucket(self, key: int) -> list[list[int]]:
        return self.buckets[key % self.bucket_count]

    def put(self, key: int, value: int) -> None:
        bucket = self._bucket(key)

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])

    def get(self, key: int) -> int:
        for stored_key, value in self._bucket(key):
            if stored_key == key:
                return value

        return -1

    def remove(self, key: int) -> None:
        bucket = self._bucket(key)

        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket.pop(index)
                return
