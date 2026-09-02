class Solution:
    def minOperations(self, nums: list[int]) -> int:
        operation_count = 0

        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                continue

            increment = nums[index - 1] + 1 - nums[index]
            nums[index] += increment
            operation_count += increment

        return operation_count
