class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []

        for num in range(left, right + 1):
            count = 0
            for x in str(num):
                x = int(x)
                if x == 0:
                    break
                if num % x == 0:
                    count += 1
            if count == len(str(num)):
                answer.append(num)

        return answer