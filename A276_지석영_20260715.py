# A276 Count of Matches in Tournament
class Solution:
    def numberOfMatches(self, n: int) -> int:
        answer = 0

        while n > 1:
            matches = n // 2
            answer += matches

            if n % 2 == 0:
                n = n // 2
            else:
                n = matches + 1

        return answer

