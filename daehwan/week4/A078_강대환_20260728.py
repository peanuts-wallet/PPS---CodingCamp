def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        h = i + 1
        
        if citations[i] >= h:
            answer = h
        else:
            break
    
    return answer