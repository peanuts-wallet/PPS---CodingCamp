# A064 Height Checker
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        answer = 0

        for index in range(len(heights)):
            if heights[index] != expected[index]:
                answer += 1

        return answer

