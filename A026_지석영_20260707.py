# A026 하샤드 수
def solution(x):
    digit_sum = 0

    for digit in str(x):
        digit_sum += int(digit)

    return x % digit_sum == 0
