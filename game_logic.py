# functions used to play the royal game of ur 

import numpy as np
import pandas as pd
import time


def init_board():
	board = np.zeros((3,4), dtype = np.int8)
	board[0,1] = 2
	board[2,1] = -2 
	return board

def game_rules():
	print()
	print("--------------------------------")
	print("Welcome to the Royal Game of Ur!")
	print("--------------------------------")
	print()
	print("How to Play")
	print("--------------------------------------------------------------------------------------------")
	print("The Royal Game of Ur is two player race to the finish.")
	print("Players will take turns rolling a die.")
	print()
	input("Press Enter to continue")
	print()
	print("This is the board")
	print("   W1 W0 W3 W2")
	print("   N1 N2 N3 N4")
	print("   B1 B0 B3 B2")
	print("Black's pieces will start from B0 and move from B0 -> B1 -> N1 -> N2 -> N3 -> N4 -> B2 -> B3")
	print("White's pieces will start from W0 and move from W0 -> W1 -> N1 -> N2 -> N3 -> N4 -> W2 -> W3")
	print()
	input("Press Enter to continue")
	print()
	print("Tiles can only hold 1 piece, except the home and end tiles.")
	print("If an enemy piece lands on your piece, then your piece is sent home.")
	print()
	input("Press Enter to continue")
	print()
	print("Each player will start with 2 pieces.")
	print("White pieces are labeled with positive signs; black pieces are labeled with negative signs.")
	print("Ex: 2 = two white pieces on the tile; -1 = one black piece on the tile; 0 = no pieces on tile")
	print("--------------------------------------------------------------------------------------------")
	print()
	input("Press Enter to start the game!")

def current_board_info(board):
	# print current board nicely 
	df_board = pd.DataFrame(board, index = ["", "", ""] ) 
	print()
	print(df_board.to_string(header=False)) # prints w/o col or index
	print()
	return 

def roll_die():
	roll = int(np.random.randint(3, size = 1))
	return roll

def current_die_info(roll):
	print("--------------------------------")
	if roll == 0:
		print("The roll is", roll, "... Bad Luck!")
	if roll != 0:
		print("The roll is ", roll)
		print("--------------------------------")
	return 

def first_player():
	print("--------------------------------")
	while True:
		try: 
			first_player = input("Who goes first? (Enter b / w): ")
			if first_player == 'b' or first_player == 'w': 
				break
			if first_player != 'b' or first_player != 'w':
				print("Oops! Invalid command. Try again")
		except ValueError:
			print("Oops! Invalid command. Try again")
	print("--------------------------------")
	return first_player

def player_choose_color():
	print("--------------------------------")
	while True:
		try: 
			player_color = input("What color would you like to be? (Enter b / w): ")
			if player_color == 'b' or player_color == 'w': 
				break
			if player_color != 'b' or player_color != 'w':
				print("Oops! Invalid command. Try again")
		except ValueError:
			print("Oops! Invalid command. Try again")
	return player_color

def play_again(game_mode):
	while True:
		try: 
			replay = input("Would you like to play again? (Enter y / n):")
			if replay == 'y' or replay == 'n':
				break
			if replay != 'y' or replay != 'n':
				print("Oops! Invalid command. Try again")
		except ValueError:
			print("Oops! Invalid command. Try again")
	if replay == 'y':
		if game_mode == 'player_vs_random':
			exec(open('player_vs_random.py').read())
		if game_mode == 'play':
			exec(open('play.py').read())
	return 


def current_player_info(player):
	if player == "w":
		print("It is White's turn!")
	if player == "b":
		print("It is Black's turn!")
	return 

def show_possible_moves(moves):
	# Used to show the possible moves nicely 
	if len(moves) == 0:
		print("No possible moves!")
		return
	input("Press Enter to show possible moves!")
	print("--------------------------------")
	for i in range(len(moves)):
		print()
		df = pd.DataFrame(moves[i], index = ["", "", ""])
		print("Possible move", i+1)
		print(df.to_string(header=False))
		print()
		time.sleep(0.5)
	return


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
			if W0 > 0 and W1 == 0: 
				new_board = board.copy()
				new_board[0,1] = W0 - 1 # W0 subtracts 1
				new_board[0,0] = 1 # W0 -> W1
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
			if N4 == 1 and W2 == 0:
				new_board = board.copy()
				new_board[1,3] = 0 # N4 becomes 0 
				new_board[0,3] = 1 # N4 -> W2
				poss_moves.append(new_board)		
			if W2 == 1:
				new_board = board.copy()
				new_board[0,3] = 0 # W2 becomes 0 
				new_board[0,2] = W3 + 1 # W2 -> W3
				poss_moves.append(new_board)
		if roll == 2:
			if W0 > 0 and N1 != 1: 
				new_board = board.copy()
				new_board[0,1] = W0 - 1 # W0 subtracts 1
				new_board[1,0] = 1 # W0 -> N1 empty
				if N1 == -1: # W0 -> N1 black; send black home
					new_board[2,1] = B0 - 1
				poss_moves.append(new_board)	
			if W1 == 1 and N2 != 1: 
				new_board = board.copy()
				new_board[0,0] = 0 # W1 becomes 0
				new_board[1,1] = 1 # W1 -> N2 empty
				if N2 == -1: # W1 -> N2 black; send black home
					new_board[2,1] = B0 - 1
				poss_moves.append(new_board)			
			if N1 == 1 and N3 != 1: 
				new_board = board.copy()
				new_board[1,0] = 0 # N1 becomes 0
				new_board[1,2] = 1 # N1 -> N3 empty
				if N3 == -1: # N1 -> N3 black; send black home
					new_board[2,1] = B0 - 1
				poss_moves.append(new_board)	
			if N2 == 1 and N4 != 1: 
				new_board = board.copy()
				new_board[1,1] = 0 # N2 becomes 0
				new_board[1,3] = 1 # N2 -> N4 empty
				if N4 == -1: # N2 -> N4 black; send black home
					new_board[2,1] = B0 - 1
				poss_moves.append(new_board)	
			if N3 == 1 and W2 == 0:
				new_board = board.copy()
				new_board[1,2] = 0 # N3 becomes 0 
				new_board[0,3] = 1 # N3 -> W2
				poss_moves.append(new_board)	
			if N4 == 1:
				new_board = board.copy()
				new_board[1,3] = 0 # N4 becomes 0 
				new_board[0,2] = W3 + 1 # N4 -> W3
				poss_moves.append(new_board)					
	if player_turn == "b":
		if roll == 1: 
			if B0 < 0 and B1 == 0: # B0 -> B1 
				new_board = board.copy()
				new_board[2,1] = B0 + 1 # B0 'adds' 1. Ex. -2 to -1 
				new_board[2,0] = -1 # B1 from 0 to -1 
				poss_moves.append(new_board)
			if B1 == -1 and N1 != -1:
				new_board = board.copy()
				new_board[2,0] = 0 # B1 becomes 0 
				new_board[1,0] = -1 # N1 becomes -1 
				if N1 == 1:
					new_board[0,1] = W0 + 1 # B1 -> N1 white; send white home
				poss_moves.append(new_board)
			if N1 == -1 and N2 != -1: # N1 -> N2 
				new_board = board.copy()
				new_board[1,0] = 0 # N1 becomes 0 
				new_board[1,1] = -1 # N2 becomes -1
				if N2 == 1:
					new_board[0,1] = W0 + 1 # N1 -> N2 white; send white home
				poss_moves.append(new_board)
			if N2 == -1 and N3 != -1: # N2 -> N3 
				new_board = board.copy()
				new_board[1,1] = 0 # N2 becomes 0 
				new_board[1,2] = -1 # N3 becomes -1
				if N3 == 1:
					new_board[0,1] = W0 + 1 # N2 -> N3 white; send white home
				poss_moves.append(new_board)
			if N3 == -1 and N4 != -1: # N3 -> N4 
				new_board = board.copy()
				new_board[1,2] = 0 # N3 becomes 0 
				new_board[1,3] = -1 # N4 becomes -1
				if N4 == 1:
					new_board[0,1] = W0 + 1 # N2 -> N3 white; send white home
				poss_moves.append(new_board)
			if N4 == -1 and B2 == 0: # N4 -> B2
				new_board = board.copy()
				new_board[1,3] = 0 # N4 becomes 0 
				new_board[2,3] = -1 # B2 becomes -1 
				poss_moves.append(new_board)
			if B2 == -1: # B2 -> B3 
				new_board = board.copy()
				new_board[2,3] = 0 # B2 becomes 0
				new_board[2,2] = B3 - 1 # B3 'subtracts' by 1; Ex. -1 to -2 
				poss_moves.append(new_board)
		if roll == 2:
			if B0 < 0 and N1 != -1: # B0 -> N1 
				new_board = board.copy()
				new_board[2,1] = B0 + 1 # B0 'increases' by 1; Ex. -1 to 0 
				new_board[1,0] = -1 # N1 becomes -1 
				if N1 == 1: # B0 -> N1 white
					new_board[0,1] = W0 + 1 # W0 increases by 1; Ex. 0 to 1 
				poss_moves.append(new_board)
			if B1 == -1 and N2 != -1: # B1 -> N2 
				new_board = board.copy()
				new_board[2,0] = 0 # B1 becomes 0
				new_board[1,1] = -1 # N2 becomes -1
				if N2 == 1: # B1 -> N2 white; send white home 
					new_board[0,1] = W0 + 1 # W0 increases by 1; Ex 0 to 1 
				poss_moves.append(new_board)
			if N1 == -1 and N3 != -1: # N1 -> N3 
				new_board = board.copy()
				new_board[1,0] = 0 # N1 becomes 0
				new_board[1,2] = -1 # N3 becomes -1
				if N3 == 1: # N1 -> N3 white; send white home 
					new_board[0,1] = W0 + 1 # W0 increases by 1; Ex 0 to 1 
				poss_moves.append(new_board)
			if N2 == -1 and N4 != -1: # N2 -> N4 
				new_board = board.copy()
				new_board[1,1] = 0 # N2 becomes 0
				new_board[1,3] = -1 # N4 becomes -1
				if N4 == 1: # N2 -> N4 white; send white home 
					new_board[0,1] = W0 + 1 # W0 increases by 1; Ex 0 to 1 
				poss_moves.append(new_board)
			if N3 == -1 and B2 != -1: # N3 -> B2 
				new_board = board.copy()
				new_board[1,2] = 0 # N3 becomes 0
				new_board[2,3] = -1 # B2 becomes -1
				poss_moves.append(new_board)
			if N4 == -1: # N4 -> B3 
				new_board = board.copy()
				new_board[1,3] = 0 # N4 becomes 0
				new_board[2,2] = B3 - 1 # B3 decreases by 1; Ex -1 to -2
				poss_moves.append(new_board)

	return poss_moves

def choose_move_num(moves):
	while True: 
		try:
			move_num = int(input("Choose a move (Enter move number): "))
			if (move_num - 1) in range(len(moves)):
				break
			if (move_num - 1) not in range(len(moves)):
				print("Oops! Invalid move. Try again")
		except ValueError:
			print("Oops! Invalid move. Try again")

	return move_num

def choose_move(move_num, moves):
	move = moves[move_num - 1]
	return move

def change_player(player):
	if player == 'w':
		new_player = 'b'
		return new_player
	if player == 'b':
		new_player = 'w'
		return new_player

def player_win(board):
	if board[0,2] == 2:
		print("White has won the game!")
		current_board_info(board)
		return True
	if board[2,2] == -2:
		print("Black has won the game!")
		current_board_info(board)
		return True
	return False







