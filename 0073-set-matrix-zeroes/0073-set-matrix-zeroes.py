class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_idx = set()
        col_idx = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row_idx.add(i)
                    col_idx.add(j)

        for i in row_idx:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0

        for i in range(len(matrix)):
            for j in col_idx:
                matrix[i][j] = 0
        

        