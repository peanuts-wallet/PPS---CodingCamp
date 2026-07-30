class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        count = {}
        first = {}
        last = {}
        
        for i in range(len(nums)):
            num = nums[i]
            
            if num not in first:
                first[num] = i
            
            last[num] = i
            
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        degree = max(count.values())
        answer = len(nums)
        
        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] + 1
                answer = min(answer, length)
        
        return answer