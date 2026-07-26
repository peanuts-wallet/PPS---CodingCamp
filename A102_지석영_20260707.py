# A102 Transpose Matrix
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        columns = len(matrix[0])
        answer = [[0] * rows for _ in range(columns)]

        for row in range(rows):
            for column in range(columns):
                answer[column][row] = matrix[row][column]

        return answer
