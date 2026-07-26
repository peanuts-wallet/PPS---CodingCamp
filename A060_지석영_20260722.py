# A060 Baseball Game
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for operation in operations:
            if operation == '+':
                new_score = scores[-1] + scores[-2]
                scores.append(new_score)

            elif operation == 'D':
                new_score = scores[-1] * 2
                scores.append(new_score)

            elif operation == 'C':
                scores.pop()

            else:
                scores.append(int(operation))

        return sum(scores)
