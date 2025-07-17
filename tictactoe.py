def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("-" * 9)
def check_winner(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],[0, 3, 6], 
        [1, 4, 7], [2, 5, 8],[0, 4, 8], [2, 4, 6]]
    return any(all(board[i] == player for i in pattern) for pattern in win_patterns)
def is_board_full(board):
    return all(cell != ' ' for cell in board)
def get_empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == ' ']
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 10 - depth
    if check_winner(board, 'X'):
        return depth - 10
    if is_board_full(board):
        return 0
    if is_maximizing:
        best_score = -float('inf')
        for i in get_empty_cells(board):
            board[i] = 'O'
            score = minimax(board, depth + 1, False, alpha, beta)
            board[i] = ' '
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for i in get_empty_cells(board):
            board[i] = 'X'
            score = minimax(board, depth + 1, True, alpha, beta)
            board[i] = ' '
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score
def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for i in get_empty_cells(board):
        board[i] = 'O'
        score = minimax(board, 0, False, -float('inf'), float('inf'))
        board[i] = ' '
        if score > best_score:
            best_score = score
            best_move = i
    return best_move
def main():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    moves_history = []  # To keep track of all moves
    print("Tic-Tac-Toe: You are X, AI is O")
    print("Enter a number (0-8) to make a move:")
    print("0 | 1 | 2")
    print("---------")
    print("3 | 4 | 5")
    print("---------")
    print("6 | 7 | 8")
    while True:
        print_board(board)
        if current_player == 'X':
            try:
                move = int(input("Your move (0-8): "))
                if move < 0 or move > 8 or board[move] != ' ':
                    print("Invalid move! Try again.")
                    continue
            except ValueError:
                print("Please enter a number between 0 and 8.")
                continue
            board[move] = 'X'
            moves_history.append(('You', move))
        else:
            print("AI is thinking...")
            move = ai_move(board)
            board[move] = 'O'
            moves_history.append(('AI', move))
        if check_winner(board, current_player):
            print_board(board)
            print(f"{'You' if current_player == 'X' else 'AI'} win!")
            print("\nMove History:")
            for turn, pos in moves_history:
                print(f"{turn} moved to position {pos}")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            print("\nMove History:")
            for turn, pos in moves_history:
                print(f"{turn} moved to position {pos}")
            break
        current_player = 'O' if current_player == 'X' else 'X'
if __name__ == "__main__":
    main()