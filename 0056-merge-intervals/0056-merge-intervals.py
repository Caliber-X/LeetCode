class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            start_previous, end_previous = output[-1]

            if start <= end_previous:
                output[-1][1] = max(end, end_previous)
            else:
                output.append([start, end])
        
        return output
        