class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        triplet_count = 0

        for first in range(len(arr) - 2):
            for second in range(first + 1, len(arr) - 1):
                if abs(arr[first] - arr[second]) > a:
                    continue

                for third in range(second + 1, len(arr)):
                    if (
                        abs(arr[second] - arr[third]) <= b
                        and abs(arr[first] - arr[third]) <= c
                    ):
                        triplet_count += 1

        return triplet_count
