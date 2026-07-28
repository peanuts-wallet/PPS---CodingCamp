class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        even = 0
        odd = 1

        for num in nums:
            if num % 2 == 0:
                ans[even] = num
                even += 2
            else:
                ans[odd] = num
                odd += 2

        return ans
