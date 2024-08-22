class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        
        # # BRUTE FORCE
        # for i in range(len(nums1)):
        #     idx = None
        #     # print(f"{i=}")
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             idx = j
        #             # print(f"{idx=}")
        #         elif nums1[i] < nums2[j] and idx is not None and j>idx:
        #             # print(f"{j=}")
        #             ans[i] = nums2[j]
        #             break

        # nums2 = [1,3,4,2,5]
        nxt_largest = {}
        stack = []
        
        for j in range(len(nums2)):
            num2 = nums2[j]
            if len(stack) == 0:
                stack.append(num2)
            else:
                if num2 > stack[-1]:
                    while len(stack) > 0 and num2 > stack[-1]:
                        nxt_largest[stack.pop()] = num2
                    stack.append(num2)
                else:
                    stack.append(num2)
            # print(f"{j=} {stack=} {nxt_largest=}")
        
        for i in range(len(nums1)):
            ans[i] = nxt_largest.get(nums1[i], -1)

        return ans

    