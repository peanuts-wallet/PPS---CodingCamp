def solution(babbling):
    answer = 0
    possible = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        prev = ""
        i = 0
        can_speak = True
        
        while i < len(word):
            found = False
            
            for sound in possible:
                if word[i:i + len(sound)] == sound and sound != prev:
                    prev = sound
                    i += len(sound)
                    found = True
                    break
            
            if not found:
                can_speak = False
                break
        
        if can_speak:
            answer += 1
    
    return answer