# A275 Sum of All Odd Length Subarrays
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        answer = 0

        for start in range(len(arr)):
            current_sum = 0

            for end in range(start, len(arr)):
                current_sum += arr[end]
                length = end - start + 1

                if length % 2 == 1:
                    answer += current_sum

        return answer

