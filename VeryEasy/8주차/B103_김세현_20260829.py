class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)

        for index in range(len(nums) - 2):
            first, second, third = nums[index : index + 3]

            if second + third > first:
                return first + second + third

        return 0
