class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for number in nums:
            index = abs(number) - 1
            nums[index] = -abs(nums[index])

        return [index + 1 for index, number in enumerate(nums) if number > 0]
