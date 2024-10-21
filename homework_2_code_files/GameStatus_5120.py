class GameStatus:

    def __init__(self, board_state, turn_O):
        self.board_state = board_state  # 2D list representing the game board
        self.turn_O = turn_O  # True if it’s O's turn, False if it’s X's turn
        self.winner = ""
        self.grid_size = len(board_state)  # Grid size (e.g., 3x3, 4x4, etc.)

    def is_terminal(self):
        # Check if the game is over (instant win for 3x3 or full board for larger grids).
        if self.grid_size == 3:
            # Traditional Tic-Tac-Toe win for 3x3 grid
            if self.check_winner("X") or self.check_winner("O"):
                return True
        else:
            # For larger grids, the game ends when the board is full
            return all(cell != "" for row in self.board_state for cell in row)
        return False

    def check_winner(self, player):
        # Check for 3 in a row for 3x3 grids (horizontal, vertical, diagonal).
        if self.grid_size == 3:
            # Check rows and columns for 3 in a row
            for i in range(3):
                if all(self.board_state[i][j] == player for j in range(3)) or all(self.board_state[j][i] == player for j in range(3)):
                    self.winner = player
                    return True

            # Check diagonals for 3 in a row
            if all(self.board_state[i][i] == player for i in range(3)) or all(self.board_state[i][2 - i] == player for i in range(3)):
                self.winner = player
                return True

        return False

    def count_triplets(self, player):
        # Count the number of triplets for a given player in grids larger than 3x3.
        if self.grid_size == 3:
            return 0  # Triplets do not apply for 3x3

        count = 0
        n = len(self.board_state)

        # Check rows and columns for triplets
        for i in range(n):
            for j in range(n - 2):  # Ensure we have space for triplets
                # Row triplet
                if self.board_state[i][j] == player and self.board_state[i][j + 1] == player and self.board_state[i][j + 2] == player:
                    count += 1
                # Column triplet
                if self.board_state[j][i] == player and self.board_state[j + 1][i] == player and self.board_state[j + 2][i] == player:
                    count += 1

        # Check diagonals for triplets
        for i in range(n - 2):
            for j in range(n - 2):
                # Main diagonal triplet
                if self.board_state[i][j] == player and self.board_state[i + 1][j + 1] == player and self.board_state[i + 2][j + 2] == player:
                    count += 1
                # Anti-diagonal triplet
                if self.board_state[i][j + 2] == player and self.board_state[i + 1][j + 1] == player and self.board_state[i + 2][j] == player:
                    count += 1

        return count

    def get_scores(self, terminal):
        # Return the score based on the current player (only after the board is full for larger grids).
        score_X = self.count_triplets("X")
        score_O = self.count_triplets("O")

        print(f"Score X: {score_X}, Score O: {score_O}")  # Debugging

        if terminal:
            if self.grid_size == 3:
                # For 3x3 grids, check for a winner based on traditional rules
                if self.winner == "X":
                    return 1  # X wins
                elif self.winner == "O":
                    return -1  # O wins
                else:
                    return 0  # Draw
            else:
                # For larger boards, return the final score based on triplet counts
                if score_X > score_O:
                    print("X wins based on final score!")
                    return 1  # X has more triplets
                elif score_O > score_X:
                    print("O wins based on final score!")
                    return -1  # O has more triplets
                else:
                    print("It's a draw based on final score!")
                    return 0  # Draw

        return 0  # In a non-terminal state, return 0

    def get_negamax_scores(self, terminal):
        # Return the negamax score based on the triplet count, without flipping scores based on turns.
        score_X = self.count_triplets("X")
        score_O = self.count_triplets("O")

        print(f"Negamax - Score X: {score_X}, Score O: {score_O}")  # Debugging

        if terminal:
            if self.grid_size == 3:
                # For 3x3 grids, return 1 for X win, -1 for O win, 0 for draw
                if self.winner == "X":
                    return 1  # X wins
                elif self.winner == "O":
                    return -1  # O wins
                else:
                    return 0  # Draw
            else:
                # For larger grids, return the final score based on triplet counts (no turn flipping)
                if score_X > score_O:
                    print("X wins (negamax)!")
                    return 1  # X has more triplets
                elif score_O > score_X:
                    print("O wins (negamax)!")
                    return -1  # O has more triplets
                else:
                    print("It's a draw (negamax)!")
                    return 0  # Draw

        return 0  # In a non-terminal state, return 0

    def get_moves(self):
        # Return all empty cells as possible moves.
        return [(i, j) for i in range(len(self.board_state)) for j in range(len(self.board_state[i])) if self.board_state[i][j] == ""]

    def get_new_state(self, move):
        # Create a new board state with the move applied.
        new_board_state = [row[:] for row in self.board_state]
        x, y = move
        new_board_state[x][y] = "O" if self.turn_O else "X"
        return GameStatus(new_board_state, not self.turn_O)  # Switch turn
