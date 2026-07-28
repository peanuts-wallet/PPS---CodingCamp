# A121 Degree of an Array
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        first_position = {}
        last_position = {}

        for index, number in enumerate(nums):
            if number not in first_position:
                first_position[number] = index

            last_position[number] = index
            count[number] = count.get(number, 0) + 1

        degree = max(count.values())
        answer = len(nums)

        for number in count:
            if count[number] == degree:
                length = last_position[number] - first_position[number] + 1
                answer = min(answer, length)

        return answer

