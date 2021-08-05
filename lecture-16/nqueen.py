class Solution:
    def solveNQueens(self, n: int):

        chess = []
        for r in range(n):
            chess.append([False] * n)

        self.solutions = []

        self.solve_nqueen(chess)

        return self.solutions

    def convert(self, avail):
        if avail:
            return "Q"
        else:
            return "."

    def solve_nqueen(self, board, row=0):

        if row == len(board):
            solution = []
            for line in board:
                solution.append("".join(map(self.convert, line)))
            self.solutions.append(solution)
            return

        for col in range(len(board)):
            if self.is_safe(board, row, col):
                board[row][col] = True
                self.solve_nqueen(board, row + 1)
                board[row][col] = False

    def is_safe(self, board, row, col):

        for index in range(1, row + 1):
            if board[row - index][col]:
                return False

            if ((col - index) >= 0) and (board[row - index][col - index]):
                return False

            if ((col + index) < len(board)) and (board[row - index][col + index]):
                return False

        return True
