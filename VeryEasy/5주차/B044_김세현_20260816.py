class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        nums = []

        for row in mat:
            for num in row:
                nums.append(num)

        result = []

        for i in range(r):
            result.append(nums[i * c:(i + 1) * c])

        return result