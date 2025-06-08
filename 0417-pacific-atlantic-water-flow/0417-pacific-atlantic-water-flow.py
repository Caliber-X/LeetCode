class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        visited_pac, visited_atl = set(), set()

        def dfs(r, c, visited, height_previous):

            # base case
            if (
                (r,c) in visited or
                r < 0 or r == rows or c < 0 or c == cols or
                heights[r][c] < height_previous
            ):
                return

            visited.add((r,c))
            # print((r,c))

            # traverse adjacent cells in 4 directions 
            for _r, _c in [[r+1,c], [r-1,c], [r, c+1], [r, c-1]]:
                dfs(_r, _c, visited, heights[r][c])

        for i in range(rows):
            dfs(i, 0, visited_pac, heights[i][0])
            dfs(i, cols-1, visited_atl, heights[i][cols-1])

        for j in range(cols):
            dfs(0, j, visited_pac, heights[0][j])
            dfs(rows-1, j, visited_atl, heights[rows-1][j])

        return list(visited_pac & visited_atl)
