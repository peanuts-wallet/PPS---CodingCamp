class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ''
        
        for char in s:
            if char.isalnum():
                text += char.lower()
        
        return text == text[::-1]