# BasicTwo Strategy
# In order of options:
# 1) Prioritize getting sending a piece home 
# 2) Randomly play 

# Notes
# If there are multiple moves that send an opponent's piece home, randomly choose between them. 

import random
import pandas as pd

def choose_move_num(board, player, moves, roll):

	move_num_list = [] # initialize possible move numbers 
	if len(moves) == 1:
		move_num = 1 # if only one move, choose the move 1
	
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

	# BasicTwo Strategy
	# If a piece can be sent home, prioritize sending it home. 
	# If not, play randomly 

	if len(moves) > 1: 
		for i in range(len(moves)):
			new_W0 = moves[i][0,1] # white start. Has 0, 1, or 2 pieces. labeled as 0, 1, and 2 
			new_W1 = moves[i][0,0] # white tile 1. Has 0 or 1 piece
			new_W2 = moves[i][0,3] # white tile 2. Has 0 or 1 piece
			new_W3 = moves[i][0,2] # white end. Has 0, 1, or 2 pieces

			new_N1 = moves[i][1,0] # neutral tile 1. Has 0 or 1 pieces
			new_N2 = moves[i][1,1] # neutral tile 2. Has 0 or 1 pieces
			new_N3 = moves[i][1,2] # neutral tile 3. Has 0 or 1 pieces
			new_N4 = moves[i][1,3] # neutral tile 4. Has 0 or 1 pieces

			new_B0 = moves[i][2,1] # black start. Has 0, 1, or 2 pieces
			new_B1 = moves[i][2,0] # black tile 1. Has 0 or 1 piece
			new_B2 = moves[i][2,3] # black tile 2. Has 0 or 1 piece
			new_B3 = moves[i][2,2] # black end. Has 0, 1, or 2 pieces. labeled 0, -1, and -2
			if player == "w":
				
				if roll == 1:
					
					if new_W1 == W1 - 1 and new_N1 == N1 + 2 and new_B0 == B0 - 1: # W1 -> N1 black; send black home
						move_num = i + 1
						move_num_list.append(move_num)
					
					if new_N1 == N1 - 1 and new_N2 == N2 + 2 and new_B0 == B0 - 1: # N1 -> N2 black; send black home
						move_num = i + 1
						move_num_list.append(move_num)
						
					if new_N2 == N2 - 1 and new_N3 == N3 + 2 and new_B0 == B0 - 1: # N2 -> N3 black; send black home
						move_num = i + 1
						move_num_list.append(move_num)

					if new_N3 == N3 - 1 and new_N4 == N4 + 2 and new_B0 == B0 - 1: # N3 -> N4 black; send black home
						move_num = i + 1
						move_num_list.append(move_num)
				if roll == 2:
					if new_W0 == W0 - 1 and new_N1 == N1 + 2 and new_B0 == B0 - 1: # W0 -> N1 black; send black home
						move_num = i + 1
						move_num_list.append(move_num)
					if new_W1 == W1 - 1 and new_N2 == N2 + 2 and new_B0 == B0 - 1: # W1 -> N2 black; send black home
						move_num = i + 1
						move_num_list.append(move_num)		
					if new_N1 == N1 - 1 and new_N3 == N3 + 2 and new_B0 == B0 - 1: # N1 -> N3 black; send black home
						move_num = i + 1
						move_num_list.append(move_num)		
					if new_N2 == N2 - 1 and new_N4 == N4 + 2 and new_B0 == B0 - 1: # N2 -> N4 black; send black home
						move_num = i + 1
						move_num_list.append(move_num)		
						
																			
			if player == "b":
				
				if roll == 1: 
					if new_B1 == B1 + 1 and new_N1 == N1 - 2 and new_W0 == W0 + 1: # B1 -> N1 white; send white home
						move_num = i + 1
						move_num_list.append(move_num)
					if new_N1 == N1 + 1 and new_N2 == N2 - 2 and new_W0 == W0 + 1: # N1 -> N2 white; send white home
						move_num = i + 1
						move_num_list.append(move_num)
					if new_N2 == N2 + 1 and new_N3 == N3 - 2 and new_W0 == W0 + 1: # N2 -> N3 white; send white home
						move_num = i + 1
						move_num_list.append(move_num) 
					if new_N3 == N3 + 1 and new_N4 == N4 - 2 and new_W0 == W0 + 1: # N3 -> N4 white; send white home
						move_num = i + 1
						move_num_list.append(move_num)
						
						
				if roll == 2:
					if new_B0 == B0 + 1 and new_N1 == N1 - 2 and new_W0 == W0 + 1: # B0 -> N1 white; send white home
						move_num = i + 1
						move_num_list.append(move_num)
					if new_B1 == B1 + 1 and new_N2 == N2 - 2 and new_W0 == W0 + 1: # B1 -> N2 white; send white home
						move_num = i + 1
						move_num_list.append(move_num)		
					if new_N1 == N1 + 1 and new_N3 == N3 - 2 and new_W0 == W0 + 1: # N1 -> N3 white; send white home
						move_num = i + 1
						move_num_list.append(move_num)		
					if new_N2 == N2 + 1 and new_N4 == N4 - 2 and new_W0 == W0 + 1: # N2 -> N4 white; send white home
						move_num = i + 1
						move_num_list.append(move_num)		
						
	two_desired_moves = False
	if len(move_num_list) == 1:
		move_num = random.choice(move_num_list) # choose the move number.
	if len(move_num_list) == 2:
		move_num = random.choice(move_num_list) # choose the move number. + 1 b/c human input 1 -> 0 for machine
		two_desired_moves = True
		'''
		for i in range(len(moves)):
			print()
			df = pd.DataFrame(moves[i], index = ["", "", ""])
			print("Possible move", i+1)
			print(df.to_string(header=False))
			print()
		'''
	if len(move_num_list) == 0: 
		move_num = random.choice(range(len(moves))) + 1 # choose the move number. + 1 b/c human input 1 -> 0 for machine
	
	return move_num, two_desired_moves