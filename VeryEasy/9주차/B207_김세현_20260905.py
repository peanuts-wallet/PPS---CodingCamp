from collections import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        first_counts = Counter(word1)
        second_counts = Counter(word2)

        return all(
            abs(first_counts[character] - second_counts[character]) <= 3
            for character in set(word1 + word2)
        )
