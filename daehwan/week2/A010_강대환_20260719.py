def solution(s):
    answer = len(s)
    
    for size in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:size]
        count = 1
        
        for i in range(size, len(s), size):
            current = s[i:i + size]
            
            if current == prev:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                
                prev = current
                count = 1
        
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev
        
        answer = min(answer, len(compressed))
    
    return answer