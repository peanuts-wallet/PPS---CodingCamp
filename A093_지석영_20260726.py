# A093 Merge Sorted Array
from typing import List


class Solution:
    def merge(
        self,
        nums1: List[int],
        m: int,
        nums2: List[int],
        n: int
    ) -> None:
        """
        Do not return anything.
        Modify nums1 in-place instead.
        """

        first = m - 1
        second = n - 1
        write_index = m + n - 1

        while first >= 0 and second >= 0:
            if nums1[first] > nums2[second]:
                nums1[write_index] = nums1[first]
                first -= 1
            else:
                nums1[write_index] = nums2[second]
                second -= 1

            write_index -= 1

        while second >= 0:
            nums1[write_index] = nums2[second]
            second -= 1
            write_index -= 1

