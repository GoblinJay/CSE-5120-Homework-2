from GameStatus_5120 import GameStatus


def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')):
    # Check if game is over or depth limit is reached
    terminal = game_state.is_terminal()
    if depth == 0 or terminal:
        newScores = game_state.get_scores(terminal)
        return newScores, None  # No move to make in terminal state

    best_move = None  # Will store the best move found

    if maximizingPlayer:
        # MAX (Human) player
        max_value = float('-inf')
        for move in game_state.get_possible_moves():  # Iterate through all possible moves
            # Get the new game state after the move
            new_state = game_state.get_new_state(move)
            value, _ = minimax(new_state, depth - 1, False, alpha, beta)  # Call minimax for MIN player
            
            if value > max_value:
                max_value = value
                best_move = move
            
            # Alpha-beta pruning
            alpha = max(alpha, value)
            if beta <= alpha:
                break  # Beta cutoff

        return max_value, best_move
    
    else:
         #MIN (AI) player
         min_value = float('inf')
         for move in game_state.get_possible_moves():  # Iterate through all possible moves
              #Get the new game state after the move
              new_state = game_state.get_new_state(move)
              value, _ = minimax(new_state, depth - 1, True, alpha, beta)  # Call minimax for MAX player

              if value < min_value:
                  min_value = value
                  best_move = move

              # Alpha-beta pruning
              beta = min(beta, value)
              if beta <= alpha:
                  break  # Alpha cutoff
              
         return min_value, best_move
			

	# return value, best_move
def negamax(game_status: GameStatus, depth: int, turn_multiplier: int, alpha=float('-inf'), beta=float('inf')):
	terminal = game_status.is_terminal()
	if (depth==0) or (terminal):
		scores = game_status.get_negamax_scores(terminal)
		return scores, None

	"""
    YOUR CODE HERE TO CALL NEGAMAX FUNCTION. REMEMBER THE RETURN OF THE NEGAMAX SHOULD BE THE OPPOSITE OF THE CALLING
    PLAYER WHICH CAN BE DONE USING -NEGAMAX(). THE REST OF YOUR CODE SHOULD BE THE SAME AS MINIMAX FUNCTION.
    YOU ALSO DO NOT NEED TO TRACK WHICH PLAYER HAS CALLED THE FUNCTION AND SHOULD NOT CHECK IF THE CURRENT MOVE
    IS FOR MINIMAX PLAYER OR NEGAMAX PLAYER
    RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
    
    """
    #return value, best_move