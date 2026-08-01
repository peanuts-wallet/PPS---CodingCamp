def solution(s):
    answer = True
    
    count = 0
    
    for char in s:
        if char == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            answer = False
            break
    
    if count != 0:
        answer = False

    return answer