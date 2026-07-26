# A265 Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 음수와 0으로 끝나는 수는 회문이 될 수 없음
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # 숫자의 절반만 뒤집기
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10

