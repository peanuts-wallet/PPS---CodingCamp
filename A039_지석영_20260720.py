# A039 Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            middle = (left + right) // 2
            square = middle * middle

            if square == num:
                return True
            elif square < num:
                left = middle + 1
            else:
                right = middle - 1

        return False

