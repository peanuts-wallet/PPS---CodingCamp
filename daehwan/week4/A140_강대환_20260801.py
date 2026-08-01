def solution(nums):
    answer = 0
    
    max_pick = len(nums) // 2
    kind_count = len(set(nums))
    
    if kind_count > max_pick:
        answer = max_pick
    else:
        answer = kind_count
    
    return answer