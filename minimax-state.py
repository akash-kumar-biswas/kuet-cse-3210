import math

class State:
    def __init__(self, board=None, player='X'):
        if board is None:
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
        else:
            self.board = [row[:] for row in board]
        self.player = player

    def display(self):
        print("\n".join([" | ".join(row) for row in self.board]))
        print("-" * 5)


def actions(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state.board[i][j]== ' ':
                moves.append((i,j))
    return moves

    
def result(state, action):
    new_board = [row[:] for row in state.board]
    row, col = action
    new_board[row][col] = state.player
    next_player = 'O' if state.player == 'X' else 'X'
    return State(new_board, next_player)
    
def terminal(state):
    return utility(state) is not None
    
def utility(state):
    lines = []
    for i in range(3):
        lines.append(state.board[i])
        lines.append([state.board[0][i], state.board[1][i], state.board[2][i]])
    lines.append([state.board[0][0], state.board[1][1], state.board[2][2]])
    lines.append([state.board[2][0], state.board[1][1], state.board[0][2]])
    if ['X','X', 'X'] in lines:
        return 1
    elif ['O', 'O', 'O'] in lines:
        return -1
    if all(cell != ' ' for row in state.board for cell in row):
        return 0
    return None
  

def max_value(state):
    if terminal(state) == True:
        return utility(state)
    value = -math.inf
    for action in actions(state):
        nextState = result(state, action)
        value = max(value, min_value(nextState))
    return value
  

def min_value(state):
    if terminal(state) == True:
        return utility(state)
    value = math.inf
    for action in actions(state):
        nextState = result(state, action)
        value = min(value, max_value(nextState))
    return value

def minimax(state):
    if state.player == 'X':
        bestScore = -math.inf
        bestAction = None
        for action in actions(state):
            nextState = result(state, action)
            score = min_value(nextState)
            if bestScore < score:
                bestAction = action
                bestScore = score
        return bestScore, bestAction
    
    else:
        bestScore = math.inf
        bestAction = None
        for action in actions(state):
            nextState = result(state, action)
            score = max_value(nextState)
            if bestScore > score:
                bestAction = action
                bestScore = score
        return bestScore, bestAction

def play():
    state = State()
    print("Welcome to Tic-Tac-Toe! You are O, AI is X.")
    state.display()

    while not terminal(state):
        if state.player == 'O':
            row, col = map(int, input("Enter row and col (0-2 space separated): ").split())
            if (row, col) not in actions(state):
                print("Invalid move! Try again.")
                continue
            state = result(state, (row, col))
        else:
            _, action = minimax(state)
            print(f"AI plays: {action}")
            state = result(state, action)
        state.display()

    score = utility(state)
    if score == 1:
        print("X wins!")
    elif score == -1:
        print("O wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play()