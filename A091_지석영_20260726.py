# A091 Remove Element
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_index = 0

        for number in nums:
            if number != val:
                nums[write_index] = number
                write_index += 1

        return write_index

