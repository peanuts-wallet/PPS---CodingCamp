# A172 삼총사
def solution(number):
    answer = 0

    for first in range(len(number) - 2):
        for second in range(first + 1, len(number) - 1):
            for third in range(second + 1, len(number)):
                total = number[first] + number[second] + number[third]

                if total == 0:
                    answer += 1

    return answer

