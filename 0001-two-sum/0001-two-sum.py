class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return i, j
        return []

        # hashmap = {}
        # for i, val in enumerate(nums):

        #     compliment = target - val

        #     if compliment in hashmap:
        #         return [hashmap[compliment], i]
        #     hashmap[val] = i

        # return []
