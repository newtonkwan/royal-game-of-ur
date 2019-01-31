# This will be version 2.0 of mastering the Royal Game of Ur without human knowledge 

# Implements the logic of the Royal Game of Ur: 
# 3x4 board (original is 3x8)
# shape is (row x column) 
# white piece = 1 
# black piece = -1
# no pieces = 0 
# multiple white pieces (only on home or end) would be 2, 3, 4, 5, 6
# multiple black pieces (only on home or end) would be -2, -3, -4, -5, -6 
# player variable is whose turn it is: 1 = white; -1 = black
# roll variable is the die roll from the set {0, 1, 2}

# initial boardstate 
# 0  2  0  0
# 0  0  0  0 
# 0 -2  0  0 

# accessing board
# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)

import numpy as np

class Board():

	def __init__(self, first):
		# create an 3 x 4 array initialized with all 0's 
		self.board = np.zeros((3,4))

		# initialize the white and black home tiles to 2 and -2, respectively. 
		self.board[0,1] = 2
		self.board[2,1] = -2 

		# the starting player 
		self.player = first 

		# the current die roll
		self.roll = None


	def player_turn(self):
		# tells you whose turn it is 
		if self.player == "w": 
			print("Turn: white")
		if self.player == "b":
			print("Turn: black")

	def board_state(self):
		print()
		print("This is the boardstate:")
		print()
		return self.board

	def die_roll(self):
		print("Die roll: ", self.roll)

	def game_state(self):
		print("game_state")

	def legal_moves(self, roll):
		# initialize the set of possible moves 
		moves = set()
		# makes player and roll accessible to the object 
		self.player = player 
		self.roll = roll 


