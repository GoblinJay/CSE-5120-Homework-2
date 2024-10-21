from GameStatus_5120 import GameStatus


def minimax(game_state, depth, maximizingPlayer, alpha=-float('inf'), beta=float('inf')):
    if depth == 0 or game_state.is_terminal():
        return game_state.get_scores(True), None  # Return the score and no move since we're at terminal/depth limit

    if maximizingPlayer:
        max_eval = -float('inf')
        best_move = None
        for move in game_state.get_moves():
            new_game_state = game_state.get_new_state(move)
            eval, _ = minimax(new_game_state, depth - 1, False, alpha, beta)
            if eval > max_eval:  # Compare only the evaluation score, not the tuple
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in game_state.get_moves():
            new_game_state = game_state.get_new_state(move)
            eval, _ = minimax(new_game_state, depth - 1, True, alpha, beta)
            if eval < min_eval:  # Compare only the evaluation score, not the tuple
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move


def negamax(game_state, depth, turn_multiplier, alpha=-float('inf'), beta=float('inf')):
    # Negamax algorithm with alpha-beta pruning.
    if depth == 0 or game_state.is_terminal():
        # Use `get_negamax_scores()` to get the score for negamax.
        score = game_state.get_negamax_scores(game_state.is_terminal())
        return turn_multiplier * score, None  # Return negated score for negamax.

    best_move = None
    max_eval = -float('inf')

    for move in game_state.get_moves():
        new_game_state = game_state.get_new_state(move)
        eval, _ = negamax(new_game_state, depth - 1, -turn_multiplier, -beta, -alpha)

        eval = -eval  # Negate the evaluation for the negamax algorithm.
        if eval > max_eval:
            max_eval = eval
            best_move = move

        alpha = max(alpha, eval)
        if alpha >= beta:
            break  # Alpha-beta pruning.

    return max_eval, best_move


