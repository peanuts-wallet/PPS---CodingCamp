class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        answer = []
        
        for word in words:
            word = word.lower()
            
            if len(word) <= 2:
                answer.append(word)
            else:
                answer.append(word[0].upper() + word[1:])
        
        return ' '.join(answer)