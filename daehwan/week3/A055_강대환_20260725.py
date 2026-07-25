class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        answer = ''
        count = 0
        
        for char in s:
            if char == '(':
                if count > 0:
                    answer += char
                count += 1
            else:
                count -= 1
                if count > 0:
                    answer += char
        
        return answer