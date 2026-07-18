def solution(k, score):
    answer = []
    hall = []
    
    for s in score:
        hall.append(s)
        hall.sort(reverse=True)
        
        if len(hall) > k:
            hall.pop()
        
        answer.append(min(hall))
    
    return answer
