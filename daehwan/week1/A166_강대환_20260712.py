def solution(t, p):
    answer = 0
    
    p_len = len(p)
    p_num = int(p)
    
    for i in range(len(t) - p_len + 1):
        part = t[i:i + p_len]
        
        if int(part) <= p_num:
            answer += 1
    
    return answer