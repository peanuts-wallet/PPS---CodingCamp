# A118 Move Zeroes
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write_index = 0

        for number in nums:
            if number != 0:
                nums[write_index] = number
                write_index += 1

        while write_index < len(nums):
            nums[write_index] = 0
            write_index += 1
