from GameStatus_5120 import GameStatus


def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')):
    # Check if game is over or depth limit is reached
    terminal = game_state.is_terminal()
    if depth == 0 or terminal:
        newScores = game_state.get_scores(terminal)
        return newScores, None  # No move to make in terminal state

    best_move = None  # Will store the best move found

    # Check if it's the maximizing player's turn
    if maximizingPlayer:
        value = float('-inf')  # Start with the lowest possible value
        pos_moves = game_state.get_moves()  # Get all possible moves for this state

        # Iterate through all possible moves
        for move in pos_moves:
            # Get the new game state after the move
            new_game_state = game_state.get_new_state(move)

            # Recursively call minimax for the opponent's turn (minimizing player)
            best_score = minimax(new_game_state, depth - 1, False, alpha, beta)[0]

            # If this move is better than the current best, update value and best_move
            if best_score > value:
                value = best_score
                best_move = move

            # Alpha-beta pruning: if value exceeds beta, stop searching
            if value >= beta:
                break
            # Update alpha
            alpha = max(alpha, value)

    # Minimizing player's turn
    else:
        value = float('inf')  # Start with the highest possible value
        pos_moves = game_state.get_moves()  # Get all possible moves for this state

        # Iterate through all possible moves
        for move in pos_moves:
            # Get the new game state after the move
            new_game_state = game_state.get_new_state(move)

            # Recursively call minimax for the opponent's turn (maximizing player)
            min_score = minimax(new_game_state, depth - 1, True, alpha, beta)[0]

            # If this move is better than the current best, update value and best_move
            if min_score < value:
                value = min_score
                best_move = move

            # Alpha-beta pruning: if value is less than or equal to alpha, stop searching
            if value <= alpha:
                break
            # Update beta
            beta = min(beta, value)

    return value, best_move

def negamax(game_status: GameStatus, depth: int, turn_multiplier: int, alpha=float('-inf'), beta=float('inf')):
    # Check if game is in a terminal state or depth limit is reached
    terminal = game_status.is_terminal()
    if (depth == 0) or terminal:
        # Get the score from the current game state
        scores = game_status.get_negamax_scores(terminal)
        return turn_multiplier * scores, None  # Multiply by turn_multiplier to flip perspective

    best_move = None  # Initialize best_move to None
    max_value = float('-inf')  # Start with negative infinity for maximization
    pos_moves = game_status.get_moves()  # Get all possible moves

    # Iterate through all possible moves
    for move in pos_moves:
        # Generate the new game state after applying the move
        new_game_state = game_status.get_new_state(move)

        # Recursively call negamax for the opponent's move (flip the player's turn with -turn_multiplier)
        best_value = -negamax(new_game_state, depth - 1, -turn_multiplier, -beta, -alpha)[0]

        # Update max_value and best_move if a better value is found
        if best_value > max_value:
            max_value = best_value
            best_move = move

        # Update alpha for alpha-beta pruning
        alpha = max(alpha, best_value)

        # If alpha is greater than or equal to beta, prune the remaining branches (beta cutoff)
        if alpha >= beta:
            break

    # Return the best value and the best move found
    return max_value, best_move

