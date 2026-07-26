# A061 Excel Sheet Column Title
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ""

        while columnNumber > 0:
            columnNumber -= 1

            remainder = columnNumber % 26
            answer = chr(ord('A') + remainder) + answer

            columnNumber //= 26

        return answer

