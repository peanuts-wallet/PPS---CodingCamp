class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        counts = {}

        for number in arr1:
            counts[number] = counts.get(number, 0) + 1

        answer = []

        for number in arr2:
            answer.extend([number] * counts.pop(number))

        for number in sorted(counts):
            answer.extend([number] * counts[number])

        return answer
