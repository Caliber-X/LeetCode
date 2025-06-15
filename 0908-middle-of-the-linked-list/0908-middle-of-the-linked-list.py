# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p_fast, p_slow = head, head
        while p_fast is not None and p_fast.next is not None:
            p_fast = p_fast.next.next
            p_slow = p_slow.next
        return p_slow