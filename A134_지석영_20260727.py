# A134 Reverse Prefix of Word
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)

        if index == -1:
            return word

        reversed_part = word[:index + 1][::-1]
        remaining_part = word[index + 1:]

        return reversed_part + remaining_part

