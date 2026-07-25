class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        answer = strs[0]
        
        for word in strs[1:]:
            while not word.startswith(answer):
                answer = answer[:-1]
                
                if answer == "":
                    return ""
        
        return answer