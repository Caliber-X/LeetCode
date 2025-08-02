class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_count = 0
        count = 0

        def dfs(r, c):
            nonlocal count

            # if out of bounds
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return

            # if water, or land is visited
            if grid[r][c] != 1:
                return

            # 1, land
            grid[r][c] = 2
            count += 1
            # print(f"{count=}")

            for r_offset, c_offset in [(0,1), (1,0), (-1,0), (0,-1)]:
                dfs(r+r_offset, c+c_offset)

                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 1:
                    continue
                # print(r,c)
                count = 0
                dfs(r,c)
                max_count = max(max_count, count)
        
        return max_count
