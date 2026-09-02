class Solution:
    def countEven(self, num: int) -> int:
        return sum(
            sum(map(int, str(number))) % 2 == 0 for number in range(1, num + 1)
        )
