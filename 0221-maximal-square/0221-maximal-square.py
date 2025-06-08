class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """recursion"""
        rows, cols = len(matrix), len(matrix[0])
        cache = {}

        def recurse(r, c):
            if r == rows or c == cols:
                return 0

            if (r,c) in cache:
                return cache[(r,c)]

            bottom = recurse(r+1, c)
            right = recurse(r, c+1)
            diag = recurse(r+1, c+1)

            cache[(r,c)] = 0
            if matrix[r][c] == "1":
                cache[(r,c)] = 1 + min(bottom, right, diag)
            
            return cache[(r,c)]

        recurse(0, 0)
        return max(cache.values()) ** 2

    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     pass
