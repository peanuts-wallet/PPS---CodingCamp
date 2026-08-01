def solution(numbers):
    answer = -1
    
    total = 0
    
    for i in range(10):
        if i not in numbers:
            total += i
    
    answer = total
    
    return answer