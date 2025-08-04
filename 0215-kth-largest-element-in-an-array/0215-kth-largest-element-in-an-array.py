class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [*map(lambda x: -x, nums)]
        heapq.heapify(nums)

        for _ in range(k):
            val = heapq.heappop(nums)
            
        return -val
