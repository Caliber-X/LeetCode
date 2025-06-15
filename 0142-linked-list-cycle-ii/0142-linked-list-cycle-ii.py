# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        
        cyclic = False
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                cyclic = True
                break
        
        if not cyclic:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
