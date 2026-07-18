def solution(N, stages):
    answer = []
    total = len(stages)
    failure = []
    
    for stage in range(1, N + 1):
        count = stages.count(stage)
        
        if total == 0:
            fail_rate = 0
        else:
            fail_rate = count / total
        
        failure.append((stage, fail_rate))
        total -= count
    
    failure.sort(key=lambda x: (-x[1], x[0]))
    
    for stage, rate in failure:
        answer.append(stage)
    
    return answer