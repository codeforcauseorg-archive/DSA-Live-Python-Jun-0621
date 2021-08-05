# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board) -> None:
        self.solve_sudoku(board)

    def solve_sudoku(self, board, row=0, col=0):

        if row == 9:
            return True

        if col == 9:
            return self.solve_sudoku(board, row + 1, 0)

        found = False

        if board[row][col] == ".":
            for value in range(1, 10):
                if self.is_safe(board, row, col, value):
                    board[row][col] = str(value)
                    done = self.solve_sudoku(board, row, col + 1)
                    if not done:
                        board[row][col] = "."
                    else:
                        found = True
                        break
        else:
            found = found or self.solve_sudoku(board, row, col + 1)

        return found

    def is_safe(self, board, row, col, value):

        value = str(value)
        for r in range(9):
            if board[r][col] == value:
                return False

        for c in range(9):
            if board[row][c] == value:
                return False

        r_p = row - (row % 3)
        c_p = col - (col % 3)
        for r in range(3):
            for c in range(3):
                if board[r_p + r][c_p + c] == value:
                    return False

        return True
