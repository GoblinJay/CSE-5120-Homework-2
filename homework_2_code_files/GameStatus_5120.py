# -*- coding: utf-8 -*-


class GameStatus:


	def __init__(self, board_state, turn_O):

		self.board_state = board_state
		self.turn_O = turn_O
		self.oldScores = 0

		self.winner = ""


	def is_terminal(self):
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
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		check_point = 3 if terminal else 2

		#Customize the scores for Negamax
		human_score = 100
		ai_score = -100

		#Check horizontal
		for row in self.board_state:
			for i in range(cols - check_point + 1): #Checks for triplets/pairs in each row
				triplet = row[i:i+check_point]
				if all(x == 1 for x in triplet):
					scores += human_score #Human player
				elif all(x == -1 for x in triplet):
					scores += ai_score #AI player

		#Check vertical
		for col in range(cols):
			for row in range(rows - check_point + 1): #Checks for triplets/pairs in each column
				triplet = [self.board_state[row+i][col] for i in range(check_point)]
				if all(x == 1 for x in triplet):
					scores += human_score #Human player
				elif all(x == -1 for x in triplet):
					scores += ai_score #AI player

		#Check diagonal
		for row in range(rows - check_point + 1):
			for col in range(cols - check_point + 1):
				#From top left to bottom right
				triplet = [self.board_state[row+i][col+i] for i in range(check_point)]
				if all(x == 1 for x in triplet):
					scores += human_score #Human player
				elif all(x == -1 for x in triplet):
					scores += ai_score #AI player

				#From top right to bottom left
				triplet = [self.board_state[row+i][col+check_point-i-1] for i in range(check_point)]
				if all(x == 1 for x in triplet):
					scores += human_score #Human player
				elif all(x == -1 for x in triplet):
					scores += ai_score #AI player

		return scores
	    

	def get_moves(self):
		moves = []
		for row in range(len(self.board_state)):
			for col in range(len(self.board_state[0])):
				if self.board_state[row][col] == 0: #If the cell is empty
					moves.append((row, col)) #Append the move to the list of moves
		return moves


	def get_new_state(self, move):
		new_board_state = self.board_state.copy()
		x, y = move[0], move[1]
		new_board_state[x,y] = 1 if self.turn_O else -1
		return GameStatus(new_board_state, not self.turn_O)
