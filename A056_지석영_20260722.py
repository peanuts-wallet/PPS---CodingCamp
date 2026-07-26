# A056 Next Greater Element I
from typing import List


class Solution:
    def nextGreaterElement(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[int]:

        next_greater = {}
        stack = []

        for number in nums2:
            while stack and stack[-1] < number:
                smaller_number = stack.pop()
                next_greater[smaller_number] = number

            stack.append(number)

        while stack:
            number = stack.pop()
            next_greater[number] = -1

        answer = []

        for number in nums1:
            answer.append(next_greater[number])

        return answer

