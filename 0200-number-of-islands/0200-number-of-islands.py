class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if i < 0 or i >= R or j < 0 or j >=C:
                return
            val = grid[i][j]
            if val == "0":
                return
            if val == "2":
                return
            # val == "1"
            grid[i][j] = "2"
            for r_offset, c_offset in [(0,1), (1,0), (0,-1), (-1,0)]:
                dfs(i+r_offset, j+c_offset)

        for i in range(R):
            for j in range(C):
                val = grid[i][j]
                if val == "1":
                    count += 1
                    dfs(i, j)

        return count
