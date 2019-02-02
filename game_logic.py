# functions used to play the royal game of ur 

import numpy as np


def init_board():
	board = np.zeros((3,4))
	board[0,1] = 2
	board[2,1] = -2 
	return board

def game_rules():
	print()
	print("Welcome to the Royal Game of Ur!")
	print("--------------------------------")
	print("How to Play")
	print("This is a two-person race to the finish.")
	print("0  start  end  0")
	print("0    0     0   0")
	print("0  start  end  0")
	print("Players will take turns rolling a die and moving their pieces.")
	print("Black pieces are labeled with negative signs and white pieces are labeled with positive signs")
	print("Ex: 2 = two white pieces on the tile; -1 = one black piece on the tile; 0 = no pieces on tile")
	print("--------------------------------")
	input("Press Enter to start the game!")


def roll_die():
	roll = int(np.random.randint(3, size = 1))
	print("The roll is ", roll)
	return roll

def first_player():
	print("--------------------------------")
	first_player = input("Who goes first? (Enter b / w): ")
	print("--------------------------------")
	return first_player

def possible_moves(player_turn, board, roll):
	# W1 W0 W3 W2
	# N1 N2 N3 N4
	# B1 B0 B3 B2

	poss_moves = [] # initialize possible moves 

	W0 = board[0,1] # white start. Has 0, 1, or 2 pieces. labeled as 0, 1, and 2 
	W1 = board[0,0] # white tile 1. Has 0 or 1 piece
	W2 = board[0,3] # white tile 2. Has 0 or 1 piece
	W3 = board[0,2] # white end. Has 0, 1, or 2 pieces

	N1 = board[1,0] # neutral tile 1. Has 0 or 1 pieces
	N2 = board[1,1] # neutral tile 2. Has 0 or 1 pieces
	N3 = board[1,2] # neutral tile 3. Has 0 or 1 pieces
	N4 = board[1,3] # neutral tile 4. Has 0 or 1 pieces

	B0 = board[2,1] # black start. Has 0, 1, or 2 pieces
	B1 = board[2,0] # black tile 1. Has 0 or 1 piece
	B2 = board[2,3] # black tile 2. Has 0 or 1 piece
	B3 = board[2,2] # black end. Has 0, 1, or 2 pieces. labeled 0, -1, and -2

	if roll == 0:
		return [] # no possible moves 
	if player_turn == "w":
		if roll == 1:
			if W0 > 0 and W1 == 0: # W0 -> W1
				new_board = board.copy()
				new_board[0,1] = W0 - 1
				new_board[0,0] = 1
				poss_moves.append(new_board)
			if W1 == 1 and N1 != 1:
				new_board = board.copy()
				new_board[0,0] = 0 # W1 becomes 0
				new_board[1,0] = 1 # W1 -> N1 empty
				if N1 == -1: # W1 -> N1 black; send black home
					new_board[2,1] = B0 - 1
				poss_moves.append(new_board)
			if N1 == 1 and N2 != 1:
				new_board = board.copy()
				new_board[1,0] = 0	# N1 becomes 0 
				new_board[1,1] = 1	# N1 -> N2 empty
				if N2 == -1: # N1 -> N2 black; send black home
					new_board[2,1] = B0 - 1
				poss_moves.append(new_board)
			if N2 == 1 and N3 != 1:
				new_board = board.copy()
				new_board[1,1] = 0 # N2 becomes 0 
				new_board[1,2] = 1 # N2 -> N3 empty
				if N3 == -1: # N2 -> N3 black; send black home
					new_board[2,1] = B0 - 1
				poss_moves.append(new_board)	
			if N3 == 1 and N4 != 1:
				new_board = board.copy()
				new_board[1,2] = 0 # N3 becomes 0 
				new_board[1,3] = 1 # N3 -> N4 empty
				if N4 == -1: # N3 -> N4 black; send black home
					new_board[2,1] = B0 - 1
				poss_moves.append(new_board)						


	if player_turn == "b":
		return []

	return poss_moves

def play_game():
	return

def choose_move():
	return





