# A013 Single Number
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0

        for number in nums:
            answer ^= number

        return answer
