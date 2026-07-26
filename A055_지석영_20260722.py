# A055 Remove Outermost Parentheses
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        answer = []
        depth = 0

        for parenthesis in s:
            if parenthesis == '(':
                if depth > 0:
                    answer.append(parenthesis)

                depth += 1

            else:
                depth -= 1

                if depth > 0:
                    answer.append(parenthesis)

        return ''.join(answer)

