def solution(a, b, n):
    answer = 0
    while n >= a:
        received = (n // a) * b
        answer += received
        n = received + (n % a)
    return answer