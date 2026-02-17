SIZE = 9


def is_valid(board, row, col, num):

    if num in board[row]:
        return False

    for r in range(SIZE):
        if board[r][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True


def select_mrv_cell(board):

    min_count = float('inf')
    best_cell = None

    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:

                valid_numbers = [
                    num for num in range(1, 10)
                    if is_valid(board, r, c, num)
                ]

                if len(valid_numbers) < min_count:
                    min_count = len(valid_numbers)
                    best_cell = (r, c)

    return best_cell


def solve(board):

    cell = select_mrv_cell(board)

    if not cell:
        return True

    row, col = cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


board = [
    [5,3,0,0,7,0,0,1,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

solve(board)

for row in board:
    print(row)
