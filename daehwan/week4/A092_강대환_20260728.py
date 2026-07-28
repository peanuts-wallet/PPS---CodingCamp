class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        answer = [0] * len(nums)
        
        even_index = 0
        odd_index = 1
        
        for num in nums:
            if num % 2 == 0:
                answer[even_index] = num
                even_index += 2
            else:
                answer[odd_index] = num
                odd_index += 2
        
        return answer