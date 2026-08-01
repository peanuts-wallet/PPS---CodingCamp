def solution(word):
    answer = 0
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    def make_word(current):
        if len(current) > 5:
            return
        
        if current != '':
            words.append(current)
        
        for vowel in vowels:
            make_word(current + vowel)
    
    make_word('')
    
    for i in range(len(words)):
        if words[i] == word:
            answer = i + 1
            break
    
    return answer