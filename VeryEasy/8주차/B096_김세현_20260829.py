class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = {}

        for index, number in enumerate(nums):
            complement = target - number

            if complement in indices:
                return [indices[complement], index]

            indices[number] = index

        return []
