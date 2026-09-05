def solution(a, b):
    return sum(first * second for first, second in zip(a, b))
