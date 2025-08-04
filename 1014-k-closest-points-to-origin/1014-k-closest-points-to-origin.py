class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heap = []
        # for point in points:
        #     x,y = point
        #     dist = (x**2 + y**2)**0.5
        #     heapq.heappush(heap, (dist, point))

        # output = []
        # for _ in range(k):
        #     dist, point = heapq.heappop(heap)
        #     output.append(point)
        
        # return output

        output = heapq.nsmallest(
            k,
            map(lambda point: ((point[0]**2 + point[1]**2)**0.5, point), points),
            key=lambda x: x[0]
        )
        output = [*map(lambda x: x[1], output)]
        return output
