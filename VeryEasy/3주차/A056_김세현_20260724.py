class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []

        for num in nums1:
            index = nums2.index(num)
            bigger = -1

            for i in range(index + 1, len(nums2)):
                if nums2[i] > num:
                    bigger = nums2[i]
                    break

            answer.append(bigger)

        return answer