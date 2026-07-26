# A089 Convert Sorted Array to Binary Search Tree
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(
        self,
        nums: List[int]
    ) -> Optional[TreeNode]:

        def make_tree(left, right):
            if left > right:
                return None

            middle = (left + right) // 2

            node = TreeNode(nums[middle])
            node.left = make_tree(left, middle - 1)
            node.right = make_tree(middle + 1, right)

            return node

        return make_tree(0, len(nums) - 1)

