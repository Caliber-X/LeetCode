# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == headB:
            return headA
        pA, pB = headA, headB
        while True:
            pA = pA.next
            pB = pB.next
            if pA is None and pB is None:
                return None
            if pA is None:
                pA = headB
            elif pB is None:
                pB = headA
            if pA == pB:
                return pA
