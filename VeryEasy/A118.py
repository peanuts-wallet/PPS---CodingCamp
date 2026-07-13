class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        position = 0  # 다음 0이 아닌 숫자가 들어갈 위치

        for i in range(len(nums)):
            if nums[i] != 0:
                if i != position:
                    nums[position], nums[i] = nums[i], nums[position]

                position += 1