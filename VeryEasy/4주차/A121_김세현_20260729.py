class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        first = {}
        last = {}

        for i, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1

            if num not in first:
                first[num] = i

            last[num] = i

        degree = max(count.values())
        answer = len(nums)

        for num in count:
            if count[num] == degree:
                answer = min(answer, last[num] - first[num] + 1)

        return answer