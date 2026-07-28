# A171 콜라 문제
def solution(a, b, n):
    answer = 0

    while n >= a:
        received = (n // a) * b
        remaining = n % a

        answer += received
        n = received + remaining

    return answer

