
class Solution:

    # # O(m+n)
    # def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
    #     len1 = len(num1)
    #     len2 = len(num2)
    #     len_tot = len1 + len2
        
    #     index_of_median_values = [int(len_tot/2)] if len_tot%2 == 1 else [int(len_tot/2)-1, int(len_tot/2)]
    #     idx_median = 0

    #     print(index_of_median_values)

    #     i, j = 0, 0
    #     count = -1
    #     val = 0
        
    #     def _check_reached_median_index(count, _val):
    #         nonlocal val, idx_median
    #         if count == index_of_median_values[idx_median]:
    #             print("yesss", _val)
    #             val = (idx_median * val + _val) / (idx_median + 1)
    #             idx_median += 1
    #             if idx_median == len(index_of_median_values):
    #                 return True
    #         return False

    #     ret = False
    #     while((i < len1) and (j < len2)):
    #       print(i, j)
    #       if num1[i] < num2[j]:
    #         count += 1
    #         ret = _check_reached_median_index(count, num1[i])
    #         i += 1
    #         if ret:
    #             break

    #       else:
    #         count += 1
    #         ret = _check_reached_median_index(count, num2[j])
    #         j += 1
    #         if ret:
    #             break

    #     if ret:
    #         return val
            
    #     print(f"{idx_median = }")
    #     print(f"{val = }")
    #     print(f"{count = }")


    #     if i==len1:
    #         print("i reached end")
    #     else:
    #         print("j reached end")
    #     print(f"{i=} {j=}")

    #     while idx_median <= len(index_of_median_values):
    #         print(idx_median, index_of_median_values[idx_median], count)
    #         ret = _check_reached_median_index(index_of_median_values[idx_median], 
    #                                           num2[j-1+index_of_median_values[idx_median]-count] if i == len1 else 
    #                                           num1[i-1+index_of_median_values[idx_median]-count])
    #         print(idx_median)
    #         if ret:
    #             break
    #         # count = index_of_median_values[idx_median-1]
    #         # count += 1

    #     return val



    # O(log(m+n))
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        A, B = num1, num2
        tot = len(A) + len(B)
        half = tot // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            idx_a = (l+r) // 2
            idx_b = half - idx_a - 2

            a_left = A[idx_a] if idx_a >= 0 else float("-inf")
            a_right = A[idx_a + 1] if idx_a + 1 < len(A) else float("inf")
            b_left = B[idx_b] if idx_b >= 0 else float("-inf")
            b_right = B[idx_b + 1] if idx_b + 1 < len(B) else float("inf")

            if a_right < b_left:
                l = idx_a + 1

            elif b_right < a_left:
                r = idx_a - 1

            else:
                # corect partition
                # odd
                if tot % 2 == 1:
                    return min(a_right, b_right)

                # even
                return (max(a_left, b_left) + min(a_right, b_right)) / 2

