class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        answer = 0
        
        for num in nums:
            answer = answer ^ num
        
        return answer
