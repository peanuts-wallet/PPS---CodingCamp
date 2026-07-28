# A103 Unique Morse Code Words
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."
        ]

        transformations = set()

        for word in words:
            transformed = ""

            for character in word:
                index = ord(character) - ord('a')
                transformed += morse_codes[index]

            transformations.add(transformed)

        return len(transformations)

