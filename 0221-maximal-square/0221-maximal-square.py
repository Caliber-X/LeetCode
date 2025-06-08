class Solution:
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     """recursion"""
    #     rows, cols = len(matrix), len(matrix[0])
    #     cache = {}

    #     def recurse(r, c):
    #         if r == rows or c == cols:
    #             return 0

    #         if (r,c) in cache:
    #             return cache[(r,c)]

    #         bottom = recurse(r+1, c)
    #         right = recurse(r, c+1)
    #         diag = recurse(r+1, c+1)

    #         cache[(r,c)] = 0
    #         if matrix[r][c] == "1":
    #             cache[(r,c)] = 1 + min(bottom, right, diag)
            
    #         return cache[(r,c)]

    #     recurse(0, 0)
    #     return max(cache.values()) ** 2

    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     """recursion"""
    #     rows, cols = len(matrix), len(matrix[0])
    #     visited = set()

    #     def recurse(r, c):
    #         if r == rows or c == cols:
    #             return 0

    #         if (r,c) in visited:
    #             return matrix[r][c]

    #         bottom = recurse(r+1, c)
    #         right = recurse(r, c+1)
    #         diag = recurse(r+1, c+1)

    #         if matrix[r][c] == "1":
    #             matrix[r][c] = 1 + min(bottom, right, diag)
    #         else:
    #             matrix[r][c] = 0
    #         visited.add((r,c))
            
    #         return matrix[r][c]

    #     recurse(0, 0)
        
    #     result = 0
    #     for row in matrix:
    #         for val in row:
    #             result = max(result, val)
    #     return result ** 2

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """DP"""
        rows, cols = len(matrix), len(matrix[0])
        val_max = 0

        for i in range(rows):
            for j in range(cols):
                top = matrix[i-1][j] if i>0 and j>0 else 0
                left = matrix[i][j-1] if i>0 and j>0 else 0
                diag = matrix[i-1][j-1] if i>0 and j>0 else 0

                if matrix[i][j] == "0":
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = 1 + min(top, left, diag)
                    val_max = max(val_max, matrix[i][j])

        return val_max * val_max



        

