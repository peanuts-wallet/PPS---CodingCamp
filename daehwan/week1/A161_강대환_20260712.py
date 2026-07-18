def solution(keymap, targets):
    answer = []
    
    key_count = {}
    
    for key in keymap:
        for i in range(len(key)):
            char = key[i]
            count = i + 1
            
            if char not in key_count:
                key_count[char] = count
            else:
                key_count[char] = min(key_count[char], count)
    
    for target in targets:
        total = 0
        
        for char in target:
            if char not in key_count:
                total = -1
                break
            
            total += key_count[char]
        
        answer.append(total)
    
    return answer