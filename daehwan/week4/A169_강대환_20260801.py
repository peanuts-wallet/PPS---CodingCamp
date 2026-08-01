def solution(ingredient):
    answer = 0
    
    stack = []
    
    for food in ingredient:
        stack.append(food)
        
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            
            for i in range(4):
                stack.pop()
    
    return answer