class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x,y = point
            dist = (x**2 + y**2)**0.5
            heapq.heappush(heap, (dist, point))

        output = []
        for _ in range(k):
            dist, point = heapq.heappop(heap)
            output.append(point)
        
        return output

