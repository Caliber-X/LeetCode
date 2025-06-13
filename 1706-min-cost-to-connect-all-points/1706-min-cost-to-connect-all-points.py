import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        neighbour_cost = {}
        for i in range(N-1):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                neighbour_cost[(i,j)] = abs(x1-x2) + abs(y1-y2)

        # prim's algo
        heap = [[0,0]]
        visited = set()
        cost_min = 0
        while len(visited) < N:
            cost, idx = heapq.heappop(heap)
            if idx in visited:
                continue
            cost_min += cost
            visited.add(idx)
            for i in range(N):
                if i == idx:
                    continue
                cost = neighbour_cost[(min(i,idx), max(i,idx))]
                heapq.heappush(heap, (cost, i))

        return cost_min
            
