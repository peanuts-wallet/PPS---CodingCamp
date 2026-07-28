# A120 Find the Difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0

        for character in s:
            result ^= ord(character)

        for character in t:
            result ^= ord(character)

        return chr(result)

