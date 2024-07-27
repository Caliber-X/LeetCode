class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 1
        end = 2
        count = 2
        while True:
            if end >= len(nums):
                break
            # print(start, end, end=" -> ")
            if nums[end] > nums[start] or (nums[end] == nums[start] and nums[start] != nums[start-1]):
                # print("yes", end="")
                start += 1
                nums[start], nums[end] = nums[end], nums[start]
                count += 1
            # print(" ", nums)
            end += 1
        return count
