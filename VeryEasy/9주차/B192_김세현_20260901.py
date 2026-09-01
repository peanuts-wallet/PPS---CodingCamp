class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        second_largest, largest = sorted(nums)[-2:]

        return (largest - 1) * (second_largest - 1)
