class Solution:
    def removeDuplicates(self, s: str) -> str:
        answer = []
        
        for char in s:
            if answer and answer[-1] == char:
                answer.pop()
            else:
                answer.append(char)
        
        return ''.join(answer)