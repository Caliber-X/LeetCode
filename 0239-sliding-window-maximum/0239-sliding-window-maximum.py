from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        output = []
        for i, n in enumerate(nums):
            while len(queue) > 0 and nums[queue[-1]] <= n:
                queue.pop()
            queue.append(i)
            if queue[0] <= i-k:
                queue.popleft()
            if i >= k-1:
                output.append(nums[queue[0]])
            # print(f"{i=} {n=} {queue=} {output=}")
        return output