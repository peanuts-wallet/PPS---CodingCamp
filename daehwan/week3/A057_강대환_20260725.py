def solution(cookie):
    answer = -1
    
    n = len(cookie)
    
    for m in range(n - 1):
        left = m
        right = m + 1
        
        left_sum = cookie[left]
        right_sum = cookie[right]
        
        while left >= 0 and right < n:
            if left_sum == right_sum:
                if answer < left_sum:
                    answer = left_sum
                
                left -= 1
                right += 1
                
                if left >= 0:
                    left_sum += cookie[left]
                
                if right < n:
                    right_sum += cookie[right]
            
            elif left_sum < right_sum:
                left -= 1
                
                if left >= 0:
                    left_sum += cookie[left]
            
            else:
                right += 1
                
                if right < n:
                    right_sum += cookie[right]
    
    if answer == -1:
        return 0
    
    return answer