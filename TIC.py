
board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    """Function to print the current state of the board."""
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board):
    """Check if there is a winner or if it's a tie."""
 
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
 
    for row in board:
        if ' ' in row:
            return None
    
    return 'Tie'

def minimax(board, depth, is_maximizing, alpha, beta):
    """The Minimax function with Alpha-Beta Pruning."""
    winner = check_winner(board)
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif winner == 'Tie':
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

def best_move(board):
    """Find the best move for the AI."""
    best_score = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    """Main function to play the game."""
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
     
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))
        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Invalid move. Try again.")
            continue

        print_board(board)
        if check_winner(board):
            break

    
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = 'O'
        
        print_board(board)
        if check_winner(board):
            break

    winner = check_winner(board)
    if winner == 'X':
        print(" You win!")
    elif winner == 'O':
        print("AI wins!")
    else:
        print("tie!")


play_game()
