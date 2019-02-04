# BasicOne Strategy
# In order of options:
# 1) Prioritize getting a piece into the end tile 

import random

def choose_move_num(board, player, moves, roll):
	if len(moves) <= 1:
		move_num = random.choice(range(len(moves))) + 1 # choose the move number. + 1 b/c human input 1 -> 0 for machine
	W3 = board[0,2]
	W2 = board[0,3]
	N4 = board[1,3]
	B3 = board[2,2]
	B2 = board[2,3]
	if len(moves) > 1: 
		for i in range(len(moves)):
			if player == "w":
				if roll == 1:
					if moves[i][0,2] == W3 + 1 and moves[i][0,3] == W2 - 1: 
						move_num = i + 1
						return move_num
				if roll == 2:
					if moves[i][0,2] == W3 + 1 and moves[i][1,3] == N4 - 1:
						move_num = i + 1
						return move_num
			if player == "b":
				if roll == 1:
					if moves[i][2,2] == B3 - 1 and moves[i][2,3] == B2 + 1:
						move_num = i + 1
						return move_num 
				if roll == 2:
					if moves[i][2,2] == B3 - 1 and moves[i][1,3] == N4 + 1:
						move_num = i + 1
						return move_num

	move_num = random.choice(range(len(moves))) + 1 # choose the move number. + 1 b/c human input 1 -> 0 for machine
	
	return move_num