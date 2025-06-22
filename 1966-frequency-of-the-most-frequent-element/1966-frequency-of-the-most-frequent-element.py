class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        rolling_sum = 0
        l = 0
        maxf = 0
        for r, val in enumerate(nums) :
            rolling_sum += val 
            window_len = r-l+1
            if val * window_len <= rolling_sum + k:
                maxf = max(maxf, window_len)
            else:
                rolling_sum -= nums[l]
                l += 1
        return maxf
