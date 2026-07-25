class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        answer = []
        depth = 0
        for char in s:
            if char == '(':
                if depth > 0:
                    answer.append(char)
                depth += 1

            else:
                depth -= 1
                if depth > 0:
                    answer.append(char)

        return ''.join(answer)