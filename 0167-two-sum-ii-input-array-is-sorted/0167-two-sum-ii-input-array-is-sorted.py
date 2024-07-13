class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1

        while start < end:
            
            sum_ = numbers[start] + numbers[end]
            
            if sum_ == target:
                return [start+1, end+1]
            
            elif sum_ > target:
                end -= 1
                # numbers[start+1] + numbers[end] > target
                # sum_ = numbers[start] + numbers[end-1]

                # if sum_ == target:
                #     return [start+1, end+1]

                # if sum_ > target:
                #     end -= 2

                # else:
                #     start += 1

            
            # if sum_ < target
            else:
                start += 1


