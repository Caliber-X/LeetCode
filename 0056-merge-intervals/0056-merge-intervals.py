class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            start_previous, end_previous = output[-1]
            start, end = intervals[i]

            if end <= end_previous:
                pass
            elif start <= end_previous:
                output[-1][1] = end
            else:
                output.append(intervals[i])
        return output
        