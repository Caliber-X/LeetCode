# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # # visited using hash map
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     visited = set()
    #     while head is not None:
    #         if head in visited:
    #             return True
    #         visited.add(head)
    #         head = head.next
    #     return False

    # 2 pointer, Floyd's Tortoise and Hare
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p_slow, p_fast = head, head
        while p_fast is not None and p_fast.next is not None:
            p_slow = p_slow.next
            p_fast = p_fast.next.next
            if p_slow == p_fast:
                return True
        return False
            