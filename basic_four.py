# BasicFour
# In order of options:
# 1) Prioritize sending a piece home
# 2) Prioritize getting to the end tile 
# 3) Random play 

# Notes
# If there are multiple moves that send an opponent's piece home, randomly choose between them. 

import random
import pandas as pd 

def choose_move_num(board, player, moves, roll):
	# chooses the move number based on BasicThree Strategy 
	strategy_move_nums = [] # initialize a list of the numbers of the desired moves

	preference_one = None # keeps track if a move has move priority one
	preference_two = [] # keeps track if a move has move priority two 


	no_pref_move = False # strategy_move_nums has no preferred moves 
	one_pref1_move = False # strategy_move_nums has one move and it is the preference_one move
	one_pref2_move = False # strategy_move_nums has one move and it is the preference_two_move
	two_pref2_moves = False # strategy_move_nums has two moves and they are both preference_two_moves
	one_pref1_one_pref2_moves = False # strategy_move_nums has two moves and one is pref_one and one is pref_two



	# if there is only one move, choose that move 
	'''
	if len(moves) == 1:
		move_num = 1 
	'''

	# initialize the current board 
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

	# if there is more than one move possible, go through the strategy 
	if len(moves) >= 1:
		# if possible, get to the end tile 
		# if possible, send a piece home. if more than one option, choose randomly
		# if none of the above are possible, play randomly 

		# loop through possible moves 
		for i in range(len(moves)):

			# initialize the possible board 
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
					if new_W3 == W3 + 1 and new_W2 == W2 - 1:
						# check if you can get you to the end tile 
						move_num = i + 1
						preference_one = move_num
						strategy_move_nums.append(move_num)
					if new_W1 == W1 - 1 and new_N1 == N1 + 2 and new_B0 == B0 - 1: # W1 -> N1 black; send black home
						# if this move can't get you to the end tile, check if it can send a piece home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num)
					if new_N1 == N1 - 1 and new_N2 == N2 + 2 and new_B0 == B0 - 1: # N1 -> N2 black; send black home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num)
						
					if new_N2 == N2 - 1 and new_N3 == N3 + 2 and new_B0 == B0 - 1: # N2 -> N3 black; send black home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num)

					if new_N3 == N3 - 1 and new_N4 == N4 + 2 and new_B0 == B0 - 1: # N3 -> N4 black; send black home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num)
				
				if roll == 2:
					if new_W3 == W3 + 1 and new_N4 == N4 - 1:
						move_num = i + 1
						preference_one = move_num
						strategy_move_nums.append(move_num)
					if new_W0 == W0 - 1 and new_N1 == N1 + 2 and new_B0 == B0 - 1: # W0 -> N1 black; send black home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num)
					if new_W1 == W1 - 1 and new_N2 == N2 + 2 and new_B0 == B0 - 1: # W1 -> N2 black; send black home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num)		
					if new_N1 == N1 - 1 and new_N3 == N3 + 2 and new_B0 == B0 - 1: # N1 -> N3 black; send black home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num)		
					if new_N2 == N2 - 1 and new_N4 == N4 + 2 and new_B0 == B0 - 1: # N2 -> N4 black; send black home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num)	
			if player == "b":
				if roll == 1:
					if new_B3 == B3 - 1 and new_B2 == B2 + 1:
						move_num = i + 1
						preference_one = move_num
						strategy_move_nums.append(move_num)
					if new_B1 == B1 + 1 and new_N1 == N1 - 2 and new_W0 == W0 + 1: # B1 -> N1 white; send white home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num)
					if new_N1 == N1 + 1 and new_N2 == N2 - 2 and new_W0 == W0 + 1: # N1 -> N2 white; send white home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num)
					if new_N2 == N2 + 1 and new_N3 == N3 - 2 and new_W0 == W0 + 1: # N2 -> N3 white; send white home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num) 
					if new_N3 == N3 + 1 and new_N4 == N4 - 2 and new_W0 == W0 + 1: # N3 -> N4 white; send white home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num)					
				if roll == 2:
					if new_B3 == B3 - 1 and new_N4 == N4 + 1:
						move_num = i + 1
						preference_one = move_num
						strategy_move_nums.append(move_num)
					if new_B0 == B0 + 1 and new_N1 == N1 - 2 and new_W0 == W0 + 1: # B0 -> N1 white; send white home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num)
					if new_B1 == B1 + 1 and new_N2 == N2 - 2 and new_W0 == W0 + 1: # B1 -> N2 white; send white home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num)		
					if new_N1 == N1 + 1 and new_N3 == N3 - 2 and new_W0 == W0 + 1: # N1 -> N3 white; send white home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num)		
					if new_N2 == N2 + 1 and new_N4 == N4 - 2 and new_W0 == W0 + 1: # N2 -> N4 white; send white home
						move_num = i + 1
						preference_two.append(move_num)
						strategy_move_nums.append(move_num)				
								

	# if no moves in strategy_move_nums, choose a random move number
	if len(strategy_move_nums) == 0: 
		move_num = random.choice(range(len(moves))) + 1 # choose the move number
		no_pref_move = True

	# if only one move possible from strategy_move_nums, choose that move 
	if len(strategy_move_nums) == 1:
		move_num = strategy_move_nums[0] # choose the only move number in strategy_move_nums
		if move_num == preference_one:
			one_pref1_move = True
		if move_num in preference_two:
			one_pref2_move = True

	# if two moves possible from the desired strategy_move_nums, choose preference 2 first 
	if len(strategy_move_nums) > 1:
		if len(preference_two) == 1: 
			# choose pref2 over pref1 
			move_num = preference_two[0]
			one_pref1_one_pref2_moves = True

		if len(preference_two) > 1:
			# choose randomly between pref2 options 
			move_num = random.choice(preference_two)
			two_pref2_moves = True
			'''
		df = pd.DataFrame(board, index = ["", "", ""])
		print(df)
		for i in range(len(moves)):
			print()
			df = pd.DataFrame(moves[i], index = ["", "", ""])
			print("Possible move", i+1)
			print(df.to_string(header=False))
			print()
			'''
	#move_possibilities = [no_pref_move_poss, one_pref1_move_poss, one_pref2_move_poss, two_pref2_moves_poss, one_pref1_one_pref2_moves_poss]
	move_choices = [no_pref_move, one_pref1_move, one_pref2_move, two_pref2_moves, one_pref1_one_pref2_moves]
	return move_num, no_pref_move, one_pref1_move, one_pref2_move, two_pref2_moves, one_pref1_one_pref2_moves