from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        source_counts = Counter(s)
        target_counts = Counter(target)

        return min(
            source_counts[character] // required_count
            for character, required_count in target_counts.items()
        )
