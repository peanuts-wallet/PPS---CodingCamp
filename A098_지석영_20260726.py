# A098 Intersection of Two Linked Lists
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self,
        headA: ListNode,
        headB: ListNode
    ) -> Optional[ListNode]:

        pointer_a = headA
        pointer_b = headB

        while pointer_a is not pointer_b:
            if pointer_a is None:
                pointer_a = headB
            else:
                pointer_a = pointer_a.next

            if pointer_b is None:
                pointer_b = headA
            else:
                pointer_b = pointer_b.next

        return pointer_a

