# A040 Determine if String Halves Are Alike
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        middle = len(s) // 2

        first_count = 0
        second_count = 0

        for index in range(middle):
            if s[index] in vowels:
                first_count += 1

        for index in range(middle, len(s)):
            if s[index] in vowels:
                second_count += 1

        return first_count == second_count
