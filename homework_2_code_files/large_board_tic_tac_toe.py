import pygame
import numpy as np
from GameStatus_5120 import GameStatus
from multiAgents import minimax, negamax

class RandomBoardTicTacToe:
    def __init__(self, grid_size=3, player_symbol="X", opponent="minimax", size=(600, 600)):
        pygame.init()
        self.size = self.width, self.height = size
        self.grid_size = grid_size
        self.player_symbol = player_symbol
        self.opponent = opponent

        # Define colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (255, 0, 0)
        self.BUTTON_COLOR = (180, 180, 180)
        self.FONT_COLOR = (0, 0, 0)

        # Fonts for the game
        self.font = pygame.font.SysFont(None, 30)
        self.title_font = pygame.font.SysFont(None, 50)

        # Grid size and cell dimensions
        self.OFFSET = 5
        self.WIDTH = self.size[0] // self.grid_size - self.OFFSET
        self.HEIGHT = self.size[1] // self.grid_size - self.OFFSET

        # Initialize Pygame screen
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe")
        self.game_reset()

    def draw_board(self):
        # Draw the board and its current state.
        self.screen.fill(self.BLACK)
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                pygame.draw.rect(self.screen, self.WHITE,
                                 [(self.OFFSET + self.WIDTH) * col + self.OFFSET,
                                  (self.OFFSET + self.HEIGHT) * row + self.OFFSET,
                                  self.WIDTH, self.HEIGHT])

                if self.board[row][col] == "X":
                    self.draw_cross(col, row)
                elif self.board[row][col] == "O":
                    self.draw_circle(col, row)

        pygame.display.update()

    def draw_circle(self, col, row):
        # Draw O for the AI player.
        center = (int(col * (self.WIDTH + self.OFFSET) + self.WIDTH // 2),
                  int(row * (self.HEIGHT + self.OFFSET) + self.HEIGHT // 2))
        radius = int(self.WIDTH // 3)
        pygame.draw.circle(self.screen, self.CIRCLE_COLOR, center, radius, 6)

    def draw_cross(self, col, row):
        # Draw X for the human player.
        start_pos1 = (int(col * (self.WIDTH + self.OFFSET) + 20),
                      int(row * (self.HEIGHT + self.OFFSET) + 20))
        end_pos1 = (int((col + 1) * (self.WIDTH + self.OFFSET) - 20),
                    int((row + 1) * (self.HEIGHT + self.OFFSET) - 20))
        pygame.draw.line(self.screen, self.CROSS_COLOR, start_pos1, end_pos1, 6)

        start_pos2 = (int(col * (self.WIDTH + self.OFFSET) + 20),
                      int((row + 1) * (self.HEIGHT + self.OFFSET) - 20))
        end_pos2 = (int((col + 1) * (self.WIDTH + self.OFFSET) - 20),
                    int(row * (self.HEIGHT + self.OFFSET) + 20))
        pygame.draw.line(self.screen, self.CROSS_COLOR, start_pos2, end_pos2, 6)

    def is_game_over(self):
        # Check if the game has ended and declare the winner.
        terminal = self.game_state.is_terminal()  # Check if the game is over

        if terminal:
            self.declare_winner()  # Call the function to declare the winner based on scores
            return True
        return False

    def handle_move(self, row, col):
        # Handle a player's move.
        if self.board[row][col] == "":  # Check if the cell is empty
            if self.current_player == "X":
                self.board[row][col] = "X"
                self.draw_cross(col, row)
            else:
                self.board[row][col] = "O"
                self.draw_circle(col, row)
            
            # Update game_state after the move
            self.game_state = GameStatus(self.board, self.current_player == "O")
            
            # Check if the game is over after the move
            if not self.is_game_over():  # Only switch players if the game is not over
                self.switch_player()
        else:
            print(f"Invalid move at row: {row}, col: {col}. Cell is already occupied!")

    def switch_player(self):
        # Switch the current player.
        if self.current_player == "X":
            self.current_player = "O"
            self.play_ai()  # AI makes a move immediately
        else:
            self.current_player = "X"

    def play_ai(self):
        # AI move using Minimax or Negamax.
        game_state = GameStatus(self.board, self.current_player == "O")
        if self.opponent == "minimax":
            _, best_move = minimax(game_state, depth=3, maximizingPlayer=False)
        else:
            _, best_move = negamax(game_state, depth=3, turn_multiplier=-1)

        if best_move:
            row, col = best_move
            self.handle_move(row, col)

        # After AI's move, switch to the human player
        if not self.is_game_over():
            self.current_player = "X"

    def game_reset(self):
        # Reset the game board and start a new game.
        self.board = [["" for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.current_player = "X"
        self.game_state = GameStatus(self.board, turn_O=False)  # X starts, so turn_O is False
        self.draw_board()

    def play_game(self):
        # Main game loop.
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    # Convert pixel position to grid position
                    col = pos[0] // (self.WIDTH + self.OFFSET)
                    row = pos[1] // (self.HEIGHT + self.OFFSET)

                    if 0 <= row < self.grid_size and 0 <= col < self.grid_size:
                        self.handle_move(row, col)

            pygame.display.update()
            clock.tick(60)

        pygame.quit()

    def declare_winner(self):
        # Declare the winner based on the final scores and show game over screen.
        final_score = self.game_state.get_scores(terminal=True)
        if final_score > 0:
            winner_text = "X wins!"
        elif final_score < 0:
            winner_text = "O wins!"
        else:
            winner_text = "It's a draw!"

        # Draw Game Over screen
        self.show_game_over(winner_text)

    def show_game_over(self, winner_text):
        # Display the game over screen with options to retry or go back to the menu.
        self.screen.fill(self.WHITE)

        # Display the winner
        winner_label = self.title_font.render(winner_text, True, self.FONT_COLOR)
        self.screen.blit(winner_label, (self.width // 2 - winner_label.get_width() // 2, 150))

        # Draw buttons
        play_again_button = pygame.draw.rect(self.screen, self.BUTTON_COLOR, (self.width // 2 - 100, 300, 200, 50))
        self.screen.blit(self.font.render('Play Again', True, self.FONT_COLOR), (self.width // 2 - 50, 315))

        menu_button = pygame.draw.rect(self.screen, self.BUTTON_COLOR, (self.width // 2 - 100, 400, 200, 50))
        self.screen.blit(self.font.render('Main Menu', True, self.FONT_COLOR), (self.width // 2 - 50, 415))

        pygame.display.update()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if play_again_button.collidepoint(x, y):
                        self.game_reset()
                        waiting = False
                    elif menu_button.collidepoint(x, y):
                        main_menu()
                        waiting = False

def main_menu():
    # Show the main menu to select game options.
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Tic Tac Toe Setup")

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FONT_COLOR = (0, 0, 0)
    HIGHLIGHT_COLOR = (0, 128, 0)
    BUTTON_COLOR = (180, 180, 180)

    font = pygame.font.SysFont(None, 30)
    title_font = pygame.font.SysFont(None, 50)

    grid_size = 3
    player_symbol = "X"
    opponent = "minimax"

    def draw_menu():
        screen.fill(WHITE)

        # Title
        title = title_font.render('Tic-Tac-Toe Setup', True, FONT_COLOR)
        screen.blit(title, (180, 50))

        # Grid size selection
        board_size_label = font.render('Select Board Size:', True, FONT_COLOR)
        screen.blit(board_size_label, (50, 150))

        three_button = pygame.draw.rect(screen, HIGHLIGHT_COLOR if grid_size == 3 else BUTTON_COLOR, (300, 150, 80, 40))
        screen.blit(font.render('3x3', True, FONT_COLOR), (320, 160))

        four_button = pygame.draw.rect(screen, HIGHLIGHT_COLOR if grid_size == 4 else BUTTON_COLOR, (400, 150, 80, 40))
        screen.blit(font.render('4x4', True, FONT_COLOR), (420, 160))

        five_button = pygame.draw.rect(screen, HIGHLIGHT_COLOR if grid_size == 5 else BUTTON_COLOR, (500, 150, 80, 40))
        screen.blit(font.render('5x5', True, FONT_COLOR), (520, 160))

        # Player symbol selection
        symbol_label = font.render('Choose Symbol (X or O):', True, FONT_COLOR)
        screen.blit(symbol_label, (50, 250))

        x_button = pygame.draw.rect(screen, HIGHLIGHT_COLOR if player_symbol == "X" else BUTTON_COLOR, (300, 250, 80, 40))
        screen.blit(font.render('X', True, FONT_COLOR), (330, 260))

        o_button = pygame.draw.rect(screen, HIGHLIGHT_COLOR if player_symbol == "O" else BUTTON_COLOR, (400, 250, 80, 40))
        screen.blit(font.render('O', True, FONT_COLOR), (430, 260))

        # Opponent selection
        opponent_label = font.render('Play Against:', True, FONT_COLOR)
        screen.blit(opponent_label, (50, 350))

        minimax_button = pygame.draw.rect(screen, HIGHLIGHT_COLOR if opponent == 'minimax' else BUTTON_COLOR, (300, 350, 100, 40))
        screen.blit(font.render('Minimax', True, FONT_COLOR), (310, 360))

        negamax_button = pygame.draw.rect(screen, HIGHLIGHT_COLOR if opponent == 'negamax' else BUTTON_COLOR, (420, 350, 100, 40))
        screen.blit(font.render('Negamax', True, FONT_COLOR), (430, 360))

        # Start game button
        start_button = pygame.draw.rect(screen, BUTTON_COLOR, (350, 450, 120, 50))
        screen.blit(font.render('Start Game', True, FONT_COLOR), (355, 465))

        pygame.display.update()
        return three_button, four_button, five_button, x_button, o_button, minimax_button, negamax_button, start_button

    running = True
    while running:
        three_button, four_button, five_button, x_button, o_button, minimax_button, negamax_button, start_button = draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # Handle clicks
                if three_button.collidepoint(x, y):
                    grid_size = 3
                elif four_button.collidepoint(x, y):
                    grid_size = 4
                elif five_button.collidepoint(x, y):
                    grid_size = 5
                elif x_button.collidepoint(x, y):
                    player_symbol = "X"
                elif o_button.collidepoint(x, y):
                    player_symbol = "O"
                elif minimax_button.collidepoint(x, y):
                    opponent = "minimax"
                elif negamax_button.collidepoint(x, y):
                    opponent = "negamax"
                elif start_button.collidepoint(x, y):
                    running = False

    # Start the game with selected options
    game = RandomBoardTicTacToe(grid_size=grid_size, player_symbol=player_symbol, opponent=opponent)
    game.play_game()


if __name__ == "__main__":
    main_menu()
