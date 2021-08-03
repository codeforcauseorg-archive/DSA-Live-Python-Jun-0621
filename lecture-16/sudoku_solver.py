sudoku =   [[8, 1, 0, 0, 3, 0, 0, 2, 7],
            [0, 6, 2, 0, 5, 0, 0, 9, 0],
            [0, 7, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 6, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 2, 0, 0, 0, 4],
            [0, 0, 8, 0, 0, 5, 0, 7, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [0, 2, 0, 0, 1, 0, 7, 5, 0],
            [3, 8, 0, 0, 7, 0, 0, 4, 2]]


def solve_sudoku(board, row=0, col=0):

    if row == 9:
        for line in board:
            print(line)
        return

    if col == 9:
        solve_sudoku(board, row+1, 0)
        return

    if board[row][col] == 0:
        for value in range(1, 10):
            if is_safe(board, row, col, value):
                board[row][col] = value
                solve_sudoku(board, row, col+1)
                board[row][col] = 0
    else:
        solve_sudoku(board, row, col + 1)


def is_safe(board, row, col, value):

    for r in range(9):
        if board[r][col] == value:
            return False

    for c in range(9):
        if board[row][c] == value:
            return False

    r_p = row - (row%3)
    c_p = col - (col%3)
    for r in range(3):
        for c in range(3):
            if board[r_p+r][c_p+c] == value:
                return False

    return True

solve_sudoku(sudoku)






