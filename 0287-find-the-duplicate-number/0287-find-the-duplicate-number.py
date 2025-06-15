class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break

        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return fast
        