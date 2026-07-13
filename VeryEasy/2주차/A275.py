class Solution:
    def numberOfMatches(self, n: int) -> int:
        playedMatches = 0

        while n > 1:
            if n % 2 == 0:
                playedMatches += n // 2
                n = n // 2
            else:
                playedMatches += (n - 1) // 2
                n = (n - 1) // 2 + 1

        return playedMatches