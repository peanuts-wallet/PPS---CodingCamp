# C104 피보나치 수
def solution(n):
    previous = 0
    current = 1

    for _ in range(2, n + 1):
        next_number = (previous + current) % 1234567
        previous = current
        current = next_number

    return current

