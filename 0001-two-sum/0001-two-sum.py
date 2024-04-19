class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        for i, val in enumerate(nums):

            compliment = target - val

            if compliment in hashmap:
                return [hashmap[compliment], i]
            hashmap[val] = i

        return []
