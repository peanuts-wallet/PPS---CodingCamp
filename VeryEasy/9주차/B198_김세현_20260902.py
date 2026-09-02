class Solution:
    def reverseVowels(self, s: str) -> str:
        characters = list(s)
        vowels = set("aeiouAEIOU")
        left, right = 0, len(characters) - 1

        while left < right:
            while left < right and characters[left] not in vowels:
                left += 1
            while left < right and characters[right] not in vowels:
                right -= 1

            characters[left], characters[right] = characters[right], characters[left]
            left += 1
            right -= 1

        return "".join(characters)
