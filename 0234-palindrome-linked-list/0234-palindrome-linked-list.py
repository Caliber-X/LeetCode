# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # find center
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # reverse from center
        curr = slow
        pre = None
        nxt = None
        while curr is not None:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        rev = pre

        # compare mormal & rev
        while rev is not None:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True
