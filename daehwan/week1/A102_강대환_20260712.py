class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        answer = []
        
        row = len(matrix)
        col = len(matrix[0])
        
        for j in range(col):
            temp = []
            
            for i in range(row):
                temp.append(matrix[i][j])
            
            answer.append(temp)
        
        return answer
