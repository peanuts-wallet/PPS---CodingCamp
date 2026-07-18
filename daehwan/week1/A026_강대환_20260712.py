def solution(x):
    answer = True
    digit_sum = 0
    
    for num in str(x):
        digit_sum += int(num)
    
    if x % digit_sum == 0:
        answer = True
    else:
        answer = False
    
    return answer
