# A115 Maximum Number of Balloons
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = {}

        for character in text:
            if character in counts:
                counts[character] += 1
            else:
                counts[character] = 1

        b_count = counts.get("b", 0)
        a_count = counts.get("a", 0)
        l_count = counts.get("l", 0) // 2
        o_count = counts.get("o", 0) // 2
        n_count = counts.get("n", 0)

        return min(b_count, a_count, l_count, o_count, n_count)
