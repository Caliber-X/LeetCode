# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for i, node in enumerate(lists):
            if not node:
                continue
            heapq.heappush(heap, (node.val, i, node))

        merge = ListNode()
        ptr = merge
        while len(heap) > 0:
            val, i, node = heapq.heappop(heap)
            ptr.next = node
            ptr = ptr.next
            node = node.next
            if not node:
                continue
            heapq.heappush(heap, (node.val, i, node))

        return merge.next
