# -*- coding: utf-8 -*-


class GameStatus:


	def __init__(self, board_state, turn_O):

		self.board_state = board_state
		self.turn_O = turn_O
		self.oldScores = 0

		self.winner = ""


	def is_terminal(self):
		"""
        YOUR CODE HERE TO CHECK IF ANY CELL IS EMPTY WITH THE VALUE 0. IF THERE IS NO EMPTY
        THEN YOU SHOULD ALSO RETURN THE WINNER OF THE GAME BY CHECKING THE SCORES FOR EACH PLAYER 
        """
		#Check if there are any empty cells (value 0)
		for row in self.board_state:
			for cell in row:
				if cell == 0:
					return False #Game isn't over yet since theres still empty cells
		#If there are no empty cells then we check to see if theres a winner by calculating scores
		score = self.get_scores(True)
		if score > 0:
			self.winner = "Human" #The player wins
		elif score < 0:
			self.winner = "AI" #The AI wins
		else:
			self.winner = "Draw"
		return True #Returns true to signal the end of the game	

	def get_scores(self, terminal):
		"""
        YOUR CODE HERE TO CALCULATE THE SCORES. MAKE SURE YOU ADD THE SCORE FOR EACH PLAYER BY CHECKING 
        EACH TRIPLET IN THE BOARD IN EACH DIRECTION (HORIZONAL, VERTICAL, AND ANY DIAGONAL DIRECTION)
        
        YOU SHOULD THEN RETURN THE CALCULATED SCORE WHICH CAN BE POSITIVE (HUMAN PLAYER WINS),
        NEGATIVE (AI PLAYER WINS), OR 0 (DRAW)
        
        """        
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		check_point = 3 if terminal else 2

		#Check horizontal
		for row in self.board_state:
			for i in range(cols - check_point + 1): #Checks for triplets/pairs in each row
				triplet = row[i:i+check_point]
				if all(x == 1 for x in triplet):
					scores += 1 #Human player
				elif all(x == -1 for x in triplet):
					scores -= 1 #AI player

		#Check vertical
		for col in range(cols):
			for row in range(rows - check_point + 1): #Checks for triplets/pairs in each column
				triplet = [self.board_state[row+i][col] for i in range(check_point)]
				if all(x == 1 for x in triplet):
					scores += 1 #Human player
				elif all(x == -1 for x in triplet):
					scores -= 1 #AI player

		#Check diagonal
		for row in range(rows - check_point + 1):
			for col in range(cols - check_point + 1):
				#From top left to bottom right
				triplet = [self.board_state[row+i][col+i] for i in range(check_point)]
				if all(x == 1 for x in triplet):
					scores += 1 #Human player
				elif all(x == -1 for x in triplet):
					scores -= 1 #AI player

				#From top right to bottom left
				triplet = [self.board_state[row+i][col+check_point-i-1] for i in range(check_point)]
				if all(x == 1 for x in triplet):
					scores += 1 #Human player
				elif all(x == -1 for x in triplet):
					scores -= 1 #AI player

		return scores

	    

	def get_negamax_scores(self, terminal):
		"""
        YOUR CODE HERE TO CALCULATE NEGAMAX SCORES. THIS FUNCTION SHOULD EXACTLY BE THE SAME OF GET_SCORES UNLESS
        YOU SET THE SCORE FOR NEGAMX TO A VALUE THAT IS NOT AN INCREMENT OF 1 (E.G., YOU CAN DO SCORES = SCORES + 100 
                                                                               FOR HUMAN PLAYER INSTEAD OF 
                                                                               SCORES = SCORES + 1)
        """
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		check_point = 3 if terminal else 2
	    

	def get_moves(self):
		moves = []
		"""
        YOUR CODE HERE TO ADD ALL THE NON EMPTY CELLS TO MOVES VARIABLES AND RETURN IT TO BE USE BY YOUR
        MINIMAX OR NEGAMAX FUNCTIONS
        """
		return moves


	def get_new_state(self, move):
		new_board_state = self.board_state.copy()
		x, y = move[0], move[1]
		new_board_state[x,y] = 1 if self.turn_O else -1
		return GameStatus(new_board_state, not self.turn_O)
