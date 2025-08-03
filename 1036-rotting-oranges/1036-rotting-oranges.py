class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        M, N = len(grid), len(grid[0])

        def get_fresh_neighbors(r, c):
            neighbors = []
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc

                # out  of bounds
                if nr < 0 or nr >= M or nc < 0 or nc >= N:
                    continue

                # not a fresh orange
                if grid[nr][nc] != 1:
                    continue

                neighbors.append((nr, nc))

            return neighbors

        count_fresh = 0
        rotten = deque()
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    count_fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))
        # print(f"{count_fresh=} {rotten=}")

        # edge cases
        if count_fresh == 0:
            return 0
        elif len(rotten) == 0:
            return -1
        
        # multi source bfs
        count = -1
        while len(rotten) > 0:
            count += 1

            size = len(rotten)
            for _ in range(size):
                r,c = rotten.popleft()
                for nr, nc in get_fresh_neighbors(r,c):
                    rotten.append((nr, nc))
                    grid[nr][nc] = 2
                    count_fresh -= 1

        return count if count_fresh == 0 else -1
