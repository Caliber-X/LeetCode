class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        tot = sum(nums)
        return n*(n+1)//2 - tot
