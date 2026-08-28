class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counts = {}

        for number in nums1:
            counts[number] = counts.get(number, 0) + 1

        intersection = []

        for number in nums2:
            if counts.get(number, 0) > 0:
                intersection.append(number)
                counts[number] -= 1

        return intersection
