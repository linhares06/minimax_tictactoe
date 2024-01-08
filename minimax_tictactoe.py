import math, random, copy

PLAYER, CPU = 1, 2
MINIMAX_DEPTH = 9

def play():
    """
    Function to play a game of Tic-Tac-Toe.

    Initializes the game board, starts the game loop, and prints the winner or a draw at the end.

    Returns:
    - None
    """
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    current_player = PLAYER
    turn = 0

    while not check_winner(board, current_player) and not check_draw(board):
        """
        Main game loop.

        Continues until there is a winner or the game is a draw.

        Returns:
        - None
        """
        display_board(board)
        
        if current_player == PLAYER:
            while True:
                position = get_player_input()
                if verify_move(board, position):
                    break
                print('Invalid move, choose another position!')
        else:
            position = get_computer_move(board, MINIMAX_DEPTH - turn)

        board = make_move(position, board, current_player)
        
        # Switch player (1 -> 2, 2 -> 1)
        current_player = 3 - current_player

        turn += 1
    
    display_board(board)

    if check_winner(board, current_player):
        """
        Checks and prints the winner of the game.

        Returns:
        - None
        """
        if 3 - current_player == PLAYER:
            print('Player wins!')
        else:
            print('CPU wins!')
    else:
        print('It\'s a draw!')

def display_board(board):
    """
    Display the Tic-Tac-Toe board.

    Args:
    - board (list): List representing the Tic-Tac-Toe board.

    Returns:
    - None
    """
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('--+---+--')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('--+---+--')
    print(f'{board[6]} | {board[7]} | {board[8]}')

def make_move(position, board, player):
    """
    Make a move on the Tic-Tac-Toe board.

    Args:
    - position (int): The position on the board where the move is made (0-8).
    - board (list): List representing the Tic-Tac-Toe board.
    - player (int): Identifier for the current player (1 for Player, 2 for CPU).

    Returns:
    - list: New board after making the move.
    """
    move_board = copy.deepcopy(board)
    move_board[position] = 'X' if player == PLAYER else 'O'

    return move_board

def check_winner(board, player):
    """
    Check if a player has won the Tic-Tac-Toe game.

    Args:
    - board (list): List representing the Tic-Tac-Toe board.
    - player (int): Identifier for the player to check for a win (1 for Player, 2 for CPU).

    Returns:
    - int or None: If the specified player has won, returns the player identifier; otherwise, returns None.
    """
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2]:
            return player

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6]:
            return player

    # Check diagonals
    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return player

    return None

def check_draw(board):
    """
    Check if the Tic-Tac-Toe game is a draw by verifying if the board is full.

    Args:
    - board (list): List representing the Tic-Tac-Toe board.

    Returns:
    - bool: True if the game is a draw, False otherwise.
    """
    return all(values not in board for values in ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

def get_player_input():
    """
    Get the player's move input.

    Returns:
    - int: Player's move position (1-9).
    """
    position = input('Player, enter your move (1-9): ')

    return int(position) - 1

def get_computer_move(board, depth):
    """
    Get the computer's move based on the minimax algorithm.

    Args:
    - board (list): List representing the Tic-Tac-Toe board.
    - depth (int): Depth of the minimax algorithm.

    Returns:
    - int: Computer's move position (0-8).
    """
    move = find_best_move(board, depth)
    print(f'CPU input move: {move+1}')

    return move

def minimax(board, depth, alpha, beta, maximizing_player, player):
    """
    Implementation of the minimax algorithm for Tic-Tac-Toe.

    Args:
    - board (list): List representing the Tic-Tac-Toe board.
    - depth (int): Depth of the minimax algorithm.
    - alpha (float): Alpha value for alpha-beta pruning.
    - beta (float): Beta value for alpha-beta pruning.
    - maximizing_player (bool): True if the current player is maximizing (CPU), False otherwise.
    - player (int): Identifier for the player (1 for Player, 2 for CPU).

    Returns:
    - float: The evaluation score for the given board state.
    """
    if depth == 0 or check_winner(board, player):
        return evaluate(board, player)

    if maximizing_player:
        max_score = -math.inf
        moves = get_possible_moves(board)
        for move in moves:
            new_board = make_move(move, board, CPU)
            score = minimax(new_board, depth - 1, alpha, beta, False, CPU)
            max_score = max(max_score, score)

            alpha = max(alpha, score)
            if beta <= alpha:
                break
            
        return max_score
    
    else:
        min_score = math.inf

        for move in get_possible_moves(board):
            new_board = make_move(move, board, PLAYER)
            score = minimax(new_board, depth - 1, alpha, beta, True, PLAYER)
            min_score = min(min_score, score)

            beta = min(beta, score)
            if beta <= alpha:
                break
            
        return min_score
    
def find_best_move(board, depth):
    """
    Find the best move for the computer using the minimax algorithm.

    Args:
    - board (list): List representing the Tic-Tac-Toe board.
    - depth (int): Depth of the minimax algorithm.

    Returns:
    - int: The best move position (0-8) for the computer.
    """
    best_score = -math.inf
    best_move = None
    best_move_board = copy.deepcopy(board)

    for move in get_possible_moves(best_move_board):
        new_board = make_move(move, best_move_board, CPU)
        score = minimax(new_board, depth - 1, -math.inf, math.inf, False, CPU)
        
        if score > best_score:
            best_score = score
            best_move = move
    
    return best_move
    
def evaluate(board, player):
    """
    Evaluate the current state of the Tic-Tac-Toe board.

    Args:
    - board (list): List representing the Tic-Tac-Toe board.
    - player (int): Identifier for the player (1 for Player, 2 for CPU).

    Returns:
    - int: Positive score if the maximizing player wins, negative score if the minimizing player wins, or 0 for a tie.
    """
    winner = check_winner(board, player)

    if winner == CPU:
        return 1
    elif winner == PLAYER:
        return -1
    
    for i in range(1, 9):
        if not verify_move(board, i):
            return 0
    
    return 0

def get_possible_moves(board):
    """
    Get a list of possible moves on the Tic-Tac-Toe board.

    Args:
    - board (list): List representing the Tic-Tac-Toe board.

    Returns:
    - list: List of possible moves (positions) on the board.
    """
    moves = [i for i, v in enumerate(board) if v not in ['X', 'O']]
    random.shuffle(moves)

    return moves

def verify_move(board, move):
    """
    Verify if a move is valid on the Tic-Tac-Toe board.

    Args:
    - board (list): List representing the Tic-Tac-Toe board.
    - move (int): Move position to verify.

    Returns:
    - bool: True if the move is valid, False otherwise.
    """
    return board[move] not in ('X', 'O')

# Run the game
play()