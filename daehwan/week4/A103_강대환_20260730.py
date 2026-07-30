class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                 "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                 "..-","...-",".--","-..-","-.--","--.."]
        
        result = set()
        
        for word in words:
            change = ""
            
            for char in word:
                index = ord(char) - ord('a')
                change += morse[index]
            
            result.add(change)
        
        return len(result)