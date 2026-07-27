class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ""
        
        while columnNumber > 0:
            columnNumber -= 1
            
            num = columnNumber % 26
            answer = chr(num + ord('A')) + answer
            
            columnNumber //= 26
        
        return answer