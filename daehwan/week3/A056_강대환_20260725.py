class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        answer = []
        stack = []
        next_greater = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                prev = stack.pop()
                next_greater[prev] = num
            
            stack.append(num)
        
        for num in nums1:
            answer.append(next_greater.get(num, -1))
        
        return answer