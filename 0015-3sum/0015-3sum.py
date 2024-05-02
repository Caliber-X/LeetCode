class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # output = set()
        # for i, num in enumerate(nums):
        #     sum = -num

        #     # do 2 sum problem
        #     balance_number_dict = {}
        #     j = i+1
        #     k = len(nums)-1

        #     if j==k:
        #         break

        #     for idx in range(j,k+1):
        #         balance = sum - nums[idx]
        #         if balance in balance_number_dict.keys():
        #             output.add(tuple(sorted([num, balance, nums[idx]])))
        #         else:
        #             balance_number_dict[nums[idx]] = balance

        # return [*map(list, output)]

        
        output = []
        nums.sort() # sort the array
        print(nums)

        def incr(idx, limit_upper=len(nums)):
            idx_ = None
            for i in range(idx+1, limit_upper):
                if nums[idx] != nums[i]:
                    idx_ = i
                    break
            return idx_

        def decr(idx, limit_lower=0):
            idx_ = None
            for i in range(idx-1, limit_lower, -1):
                if nums[idx] != nums[i]:
                    idx_ = i
                    break
            return idx_

        i=0
        while i<(len(nums)-2):

            if nums[i] > 0:
                break

            j = i+1
            k = len(nums)-1
            
            while(j<k):
                
                sum = nums[i]+nums[j]+nums[k]
                # print(i, j, k, "sum =", sum, end=" -> ")
                
                if sum < 0:
                    j = incr(j,k)
                    if j is None:
                        # print()
                        break
                
                elif sum > 0:
                    k = decr(k,j)
                    if k is None:
                        # print()
                        break
                
                else:
                    output.append([nums[i],nums[j],nums[k]])
                    j = incr(j,k)
                    if j is None:
                        # print()
                        break
                    k = decr(k,j)
                    if k is None:
                        # print()
                        break
                
                # print(i,j,k)
            
            i = incr(i)
            if i is None:
                # print()
                break

        return output
