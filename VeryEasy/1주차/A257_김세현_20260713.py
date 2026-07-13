def solution(n):
    a = 0  
    b = 1  

    for _ in range(n):
        a, b = b, (a + b) % 1234567

    return a