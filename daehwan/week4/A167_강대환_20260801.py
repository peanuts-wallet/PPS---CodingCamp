def solution(food):
    answer = ''
    
    left = ''
    
    for i in range(1, len(food)):
        count = food[i] // 2
        left += str(i) * count
    
    answer = left + '0' + left[::-1]
    
    return answer