class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        minimum_difference = min(
            arr[index] - arr[index - 1] for index in range(1, len(arr))
        )

        return [
            [arr[index - 1], arr[index]]
            for index in range(1, len(arr))
            if arr[index] - arr[index - 1] == minimum_difference
        ]
