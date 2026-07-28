# A119 Guess Number Higher or Lower

# The guess API is already defined for you.
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            middle = (left + right) // 2
            result = guess(middle)

            if result == 0:
                return middle
            elif result == 1:
                left = middle + 1
            else:
                right = middle - 1

