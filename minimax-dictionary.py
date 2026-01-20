import math

def initial_state():
    return {
        "board": [[' ' for _ in range(3)] for _ in range(3)],
        "player": "X"   # AI is X, Human is O
    }

def display(state):
    board = state["board"]
    print("\n".join([" | ".join(row) for row in board]))
    print("-" * 9)

def actions(state):
    board = state["board"]
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

def result(state, action):
    board = [row[:] for row in state["board"]]  # deep copy 2D
    r, c = action
    board[r][c] = state["player"]
    next_player = 'O' if state["player"] == 'X' else 'X'
    return {"board": board, "player": next_player}

def utility(state):
    board = state["board"]
    lines = []

    # rows and columns
    for i in range(3):
        lines.append(board[i])  # row i
        lines.append([board[0][i], board[1][i], board[2][i]])  # col i

    # diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[2][0], board[1][1], board[0][2]])

    if ['X', 'X', 'X'] in lines:
        return 1
    if ['O', 'O', 'O'] in lines:
        return -1

    # draw
    if all(cell != ' ' for row in board for cell in row):
        return 0

    return None

def terminal(state):
    return utility(state) is not None

def max_value(state):
    if terminal(state):
        return utility(state)

    v = -math.inf
    for a in actions(state):
        v = max(v, min_value(result(state, a)))
    return v

def min_value(state):
    if terminal(state):
        return utility(state)

    v = math.inf
    for a in actions(state):
        v = min(v, max_value(result(state, a)))
    return v

def minimax(state):
    # AI is X (maximize), Human is O (minimize)
    if state["player"] == 'X':
        best_score = -math.inf
        best_action = None
        for a in actions(state):
            score = min_value(result(state, a))
            if score > best_score:
                best_score = score
                best_action = a
        return best_score, best_action
    else:
        best_score = math.inf
        best_action = None
        for a in actions(state):
            score = max_value(result(state, a))
            if score < best_score:
                best_score = score
                best_action = a
        return best_score, best_action

def play():
    state = initial_state()
    print("Welcome to Tic-Tac-Toe! You are O, AI is X.\n")
    display(state)

    while not terminal(state):
        if state["player"] == 'O':
            try:
                row, col = map(int, input("Enter row and col (0-2 space separated): ").split())
            except ValueError:
                print("Invalid input! Enter two numbers like: 1 2")
                continue

            if (row, col) not in actions(state):
                print("Invalid move! Try again.")
                continue

            state = result(state, (row, col))

        else:
            _, action = minimax(state)
            print(f"AI plays: {action}")
            state = result(state, action)

        display(state)

    score = utility(state)
    if score == 1:
        print("X wins! (AI)")
    elif score == -1:
        print("O wins! (You)")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play()