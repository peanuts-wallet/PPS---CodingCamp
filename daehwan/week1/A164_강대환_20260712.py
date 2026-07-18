def solution(s):
    answer = []
    last_index = {}
    
    for i in range(len(s)):
        char = s[i]
        
        if char in last_index:
            answer.append(i - last_index[char])
        else:
            answer.append(-1)
        
        last_index[char] = i
    
    return answer