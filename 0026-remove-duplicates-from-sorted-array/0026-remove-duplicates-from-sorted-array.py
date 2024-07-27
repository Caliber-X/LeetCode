class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        end = 1
        count = 1
        while True:
            if end == len(nums):
                break
            if nums[end] > nums[start]:
                start += 1
                nums[start], nums[end] = nums[end], nums[start]
                count += 1
            end += 1
        return count