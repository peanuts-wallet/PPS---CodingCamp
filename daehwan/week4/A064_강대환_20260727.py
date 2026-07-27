class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        answer = 0
        
        expected = sorted(heights)
        
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                answer += 1
        
        return answer