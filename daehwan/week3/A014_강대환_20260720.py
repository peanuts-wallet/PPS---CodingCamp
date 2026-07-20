class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        answer = []
        
        if not nums:
            return answer
        
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]
                
                if start == end:
                    answer.append(str(start))
                else:
                    answer.append(str(start) + "->" + str(end))
                
                start = nums[i]
        
        end = nums[-1]
        
        if start == end:
            answer.append(str(start))
        else:
            answer.append(str(start) + "->" + str(end))
        
        return answer