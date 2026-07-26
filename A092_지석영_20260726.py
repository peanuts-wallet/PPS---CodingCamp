# A092 Sort Array By Parity II
from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)

        even_index = 0
        odd_index = 1

        for number in nums:
            if number % 2 == 0:
                answer[even_index] = number
                even_index += 2
            else:
                answer[odd_index] = number
                odd_index += 2

        return answer

