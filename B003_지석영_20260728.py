# B003 Sum of Left Leaves
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves(
        self,
        root: Optional[TreeNode]
    ) -> int:

        if root is None:
            return 0

        answer = 0

        if (
            root.left is not None
            and root.left.left is None
            and root.left.right is None
        ):
            answer += root.left.val

        answer += self.sumOfLeftLeaves(root.left)
        answer += self.sumOfLeftLeaves(root.right)

        return answer
