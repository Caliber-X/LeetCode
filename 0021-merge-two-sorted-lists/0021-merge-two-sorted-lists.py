# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge = ListNode()
        res = merge
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                merge.next = list1
                list1 = list1.next
            else:
                merge.next = list2
                list2 = list2.next
            merge = merge.next
        if list1 is not None:
            merge.next = list1
        elif list2 is not None:
            merge.next = list2
        return res.next
        