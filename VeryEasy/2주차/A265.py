class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = []
        y = str(x)

        for ch in range(len(y) - 1, -1, -1):
            reverse.append(y[ch])

        reversed_y = "".join(reverse)

        if reversed_y == y:
            return True
        else:
            return False