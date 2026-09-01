class Solution:
    def check(self, nums: list[int]) -> bool:
        decrease_count = sum(
            nums[index] > nums[(index + 1) % len(nums)]
            for index in range(len(nums))
        )

        return decrease_count <= 1
