import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        times_dict = {}
        for start, end, weight in times:
            if start not in times_dict:
                times_dict[start] = []
            times_dict[start].append([end, weight])
        # print(times_dict)

        if k not in times_dict:
            return -1
        
        heap = [(0, k)]
        heapq.heapify(heap)
        dist = 0
        visited = set()
        
        while len(heap) > 0:
            dist_smallest, start_smallest = heapq.heappop(heap)
            # print(dist_smallest, start_smallest)
            if start_smallest in visited:
                continue
            visited.add(start_smallest)
            dist = max(dist, dist_smallest)

            if start_smallest not in times_dict:
                continue

            for end, weight in times_dict[start_smallest]:
                if end in visited:
                    continue
                heapq.heappush(heap, (dist_smallest + weight, end))

        return dist if len(visited) == n else -1

      