class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        output = []

        # create board
        board = [-1] * n

        def pretty_print(board):
            board2d = []
            for i, val in enumerate(board):
                board2d.append("."*val + "Q" + "."*(n-val-1))
            return board2d

        def noConflicts(board, col):

            for i in range(col):

                # Unique in the row
                if board[col] == board[i]:
                    return False
                # Diagonal Check
                if (col - i == abs(board[col] - board[i])):
                    return False

            return True

        def rQueens(board, col, size):

            nonlocal output
            if col == size:
                output.append(pretty_print(board))

            else:
                for i in range(size):
                    board[col] = i
                    if noConflicts(board, col):
                        rQueens(board, col + 1, size)

        rQueens(board, 0, n)

        return output
