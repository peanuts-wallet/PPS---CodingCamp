def solution(sizes):
    answer = 0
    
    max_width = 0
    max_height = 0
    
    for size in sizes:
        w = size[0]
        h = size[1]
        
        if w < h:
            w, h = h, w
        
        max_width = max(max_width, w)
        max_height = max(max_height, h)
    
    answer = max_width * max_height
    
    return answer