N = 8

def is_valid(assignment, col, row):
    for prev_col in range(N):
        if assignment[prev_col] != -1:

            prev_row = assignment[prev_col]

            if prev_row == row:
                return False

            if abs(prev_row - row) == abs(prev_col - col):
                return False

    return True


def select_mrv_column(assignment):

    min_count = float('inf')
    best_col = None

    for col in range(N):
        if assignment[col] == -1:

            valid_rows = [
                row for row in range(N)
                if is_valid(assignment, col, row)
            ]

            if len(valid_rows) < min_count:
                min_count = len(valid_rows)
                best_col = col

    return best_col


def backtrack(assignment):

    if -1 not in assignment:
        return True

    col = select_mrv_column(assignment)

    for row in range(N):
        if is_valid(assignment, col, row):
            assignment[col] = row

            if backtrack(assignment):
                return True

            assignment[col] = -1

    return False


assignment = [-1] * N
backtrack(assignment)

print("Queen positions:")
print(assignment)


def print_board(assignment):
    for row in range(N):
        for col in range(N):
            if assignment[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


print("\nBoard:")
print_board(assignment)
