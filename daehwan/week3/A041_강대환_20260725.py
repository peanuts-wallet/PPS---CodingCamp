def solution(s):
    answer = ''
    
    words = s.split(' ')
    
    for i in range(len(words)):
        word = words[i]
        
        if word == '':
            continue
        
        words[i] = word[0].upper() + word[1:].lower()
    
    answer = ' '.join(words)
    
    return answer