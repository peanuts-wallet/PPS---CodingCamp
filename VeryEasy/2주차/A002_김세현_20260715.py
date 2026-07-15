class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        answer.append([1])

        for i in range(1, numRows):
            row = [1] * (i + 1)
            for j in range(1, len(row) - 1):
                row[j] = answer[i-1][j-1] + answer[i-1][j]
            answer.append(row)
        return answer