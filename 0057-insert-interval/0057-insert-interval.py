from bisect import bisect_right

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInterval]
        
        idx = bisect_right(intervals, newInterval[0], key=lambda x:x[0])
        print(f"{idx=}")
        
        i = idx
        while (i < len(intervals)) and (newInterval[1] >= intervals[i][0]):
            i += 1
            # print(f"{i=}")
        # i -= 1
        print(f"{i=}")

        if idx>0 and i == idx and newInterval[1] <= intervals[idx-1][1]:
            print("same")
            return intervals

        intervals_new = []
        if idx>0 and intervals[idx-1][1] >= newInterval[0]:
            intervals_new = intervals[:idx]
            if len(intervals_new) != 0:
                intervals_new[-1][1] = max(intervals_new[-1][1], newInterval[1])

        else:
            intervals_new = intervals[:idx] + [newInterval]
        print(f"{intervals_new=}")

        if i>0 and len(intervals_new) != 0:
            intervals_new[-1][1] = max(intervals_new[-1][1], intervals[i-1][1])
        print(f"{intervals_new=}")

        intervals_new += intervals[i:]
        print(f"{intervals_new=}")

        return intervals_new
            

