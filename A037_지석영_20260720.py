# A037 Self Dividing Numbers
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []

        for number in range(left, right + 1):
            current = number
            possible = True

            while current > 0:
                digit = current % 10

                if digit == 0 or number % digit != 0:
                    possible = False
                    break

                current //= 10

            if possible:
                answer.append(number)

        return answer

