# A038 Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        answer = 0

        while left <= right:
            middle = (left + right) // 2

            if middle * middle <= x:
                answer = middle
                left = middle + 1
            else:
                right = middle - 1

        return answer

