class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            if num < 10:
                return num

            answer = 0
            num = str(num)

            for i in range(len(num)):
                answer += int(num[i])

            num = answer