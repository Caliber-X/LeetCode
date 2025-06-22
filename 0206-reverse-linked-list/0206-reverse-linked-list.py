# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # # iterative
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     curr = head
    #     prev = None
    #     while curr is not None:
    #         nxt = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = nxt
    #     return prev
        
    # recursive
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def recurse(curr, prev):
            if curr is None:
                return prev
            nxt = curr.next
            curr.next = prev
            return recurse(nxt, curr)
        
        curr = head
        prev = None
        return recurse(curr, prev)
    