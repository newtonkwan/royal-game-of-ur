# BasicTwo vs. BasicTwo
# an arena to match up BasicTwo vs BasicTwo in 3x4, no flower, 0-2 die Ur. 

# BasicTwo Strategy
# In order of options:
# 1) Prioritize getting sending a piece home 
# 2) Randomly play 

from game_logic import init_board, game_rules, roll_die, possible_moves, first_player, choose_move, current_player_info, show_possible_moves, current_board_info, current_die_info, choose_move_num, choose_move, change_player, player_choose_color, play_again, player_win
import basic_one
import basic_two
import random 
import time

game_rules()

num_black_wins = 0 
num_white_wins = 0 
num_black_starts = 0
num_white_starts = 0
num_zeros = 0
num_ones = 0
num_twos = 0
num_total_games = 0 
num_one_moves = 0 
num_two_moves = 0 
num_three_moves = 0
num_choose_one = 0
num_choose_two = 0 
desired_moves = 0
white_desired_moves = 0
black_desired_moves = 0 
white_chose_desired_move = 0
black_chose_desired_move = 0 
chose_desired_move = 0
two_desired_moves = 0 

print("You simulating two computers play against each other:")
print("BasicTwo vs BasicTwo")
while True:
	try: 
		num_games = int(input("How many games do you want to simulate? (Enter a number):"))
		break
	except ValueError:
		print("Oops. Invalid input. Try again")
print("Simulating", num_games, "games...")
half_games = num_games / 2
print()

time_start = time.time()
for i in range(num_games):
	board = init_board() # initialize the board 
	
	# Determine who goes first 

	# Uncomment to make Black go first
	first = 'b'

	# Uncomment to make White go first
	#first = 'w'

	# Uncomment to have each go first an equal number of times 
	'''
	if num_white_starts != half_games:
		first = 'w'
	else:
		first = 'b'
		'''

	# Uncomment to have the first player chosen randomly
	#first = random.choice(['b', 'w']) # initialize first player; will be 'b' or 'w'
	

	# First player is randomly chosen 
	#first = random.choice(['b', 'w']) # initialize first player; will be 'b' or 'w'
	if first == 'b':
		num_black_starts += 1
	if first == 'w':
		num_white_starts += 1

	current_board = board # current board 
	current_player = first # current player 

	while True:

		current_roll = roll_die() # roll die 
		
		if current_roll == 0:
			num_zeros += 1
		if current_roll == 1:
			num_ones += 1
		if current_roll == 2:
			num_twos += 1
		

		# roll a 0 
		if current_roll == 0: 
			current_player = change_player(current_player)
			continue
	
		moves = possible_moves(current_player, current_board, current_roll) # gets possible moves 

		# no possible moves 
		if len(moves) == 0: 
			current_player = change_player(current_player)
			continue

		if len(moves) == 1:
			num_one_moves += 1
		if len(moves) == 2:
			num_two_moves += 1

		#move_num = random.choice(range(len(moves))) + 1 # choose the move number. + 1 b/c human input 1 -> 0 for machine
		what_move  = basic_two.choose_move_num(current_board, current_player, moves, current_roll)

		move_num = what_move[0]
		two_moves = what_move[1]

		# if there are two moves that are desired moves, you need to take this into account 
		if two_moves == True:
			two_desired_moves += 1

		'''		
		# UNCOMMENT TO TEST
		# test new move_num
		# check scenarios where there are two moves and one of the moves is the desired move
		# and compare it to how many times the agent chooses that move 


		W0 = current_board[0,1] # white start. Has 0, 1, or 2 pieces. labeled as 0, 1, and 2 
		W1 = current_board[0,0] # white tile 1. Has 0 or 1 piece
		W2 = current_board[0,3] # white tile 2. Has 0 or 1 piece
		W3 = current_board[0,2] # white end. Has 0, 1, or 2 pieces

		N1 = current_board[1,0] # neutral tile 1. Has 0 or 1 pieces
		N2 = current_board[1,1] # neutral tile 2. Has 0 or 1 pieces
		N3 = current_board[1,2] # neutral tile 3. Has 0 or 1 pieces
		N4 = current_board[1,3] # neutral tile 4. Has 0 or 1 pieces

		B0 = current_board[2,1] # black start. Has 0, 1, or 2 pieces
		B1 = current_board[2,0] # black tile 1. Has 0 or 1 piece
		B2 = current_board[2,3] # black tile 2. Has 0 or 1 piece
		B3 = current_board[2,2] # black end. Has 0, 1, or 2 pieces. labeled 0, -1, and -2

		if len(moves) >= 1: 
	
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
				if current_player == "w":
					
					if current_roll == 1:
						
						if new_W1 == W1 - 1 and new_N1 == N1 + 2 and new_B0 == B0 - 1: # W1 -> N1 black; send black home
							desired_moves += 1
							white_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								white_chose_desired_move += 1
								
						if new_N1 == N1 - 1 and new_N2 == N2 + 2 and new_B0 == B0 - 1: # N1 -> N2 black; send black home
							desired_moves += 1
							white_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								white_chose_desired_move += 1
								
						if new_N2 == N2 - 1 and new_N3 == N3 + 2 and new_B0 == B0 - 1: # N2 -> N3 black; send black home
							desired_moves += 1
							white_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								white_chose_desired_move += 1 
								
						if new_N3 == N3 - 1 and new_N4 == N4 + 2 and new_B0 == B0 - 1: # N3 -> N4 black; send black home
							desired_moves += 1
							white_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								white_chose_desired_move += 1 

					if current_roll == 2:
						if new_W0 == W0 - 1 and new_N1 == N1 + 2 and new_B0 == B0 - 1: # W0 -> N1 black; send black home
							desired_moves += 1
							white_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								white_chose_desired_move += 1
						if new_W1 == W1 - 1 and new_N2 == N2 + 2 and new_B0 == B0 - 1: # W1 -> N2 black; send black home
							desired_moves += 1
							white_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								white_chose_desired_move += 1		
						if new_N1 == N1 - 1 and new_N3 == N3 + 2 and new_B0 == B0 - 1: # N1 -> N3 black; send black home
							desired_moves += 1
							white_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								white_chose_desired_move += 1		
						if new_N2 == N2 - 1 and new_N4 == N4 + 2 and new_B0 == B0 - 1: # N2 -> N4 black; send black home
							desired_moves += 1
							white_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								white_chose_desired_move += 1		
								
																					
				if current_player == "b":
						
					if current_roll == 1: 
						if new_B1 == B1 + 1 and new_N1 == N1 - 2 and new_W0 == W0 + 1: # B1 -> N1 white; send white home
							desired_moves += 1
							black_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								black_chose_desired_move += 1
						if new_N1 == N1 + 1 and new_N2 == N2 - 2 and new_W0 == W0 + 1: # N1 -> N2 white; send white home
							desired_moves += 1
							black_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								black_chose_desired_move += 1
						if new_N2 == N2 + 1 and new_N3 == N3 - 2 and new_W0 == W0 + 1: # N2 -> N3 white; send white home
							desired_moves += 1
							black_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								black_chose_desired_move += 1 
						if new_N3 == N3 + 1 and new_N4 == N4 - 2 and new_W0 == W0 + 1: # N3 -> N4 white; send white home
							desired_moves += 1
							black_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								black_chose_desired_move += 1 
								
						
					if current_roll == 2:
						if new_B0 == B0 + 1 and new_N1 == N1 - 2 and new_W0 == W0 + 1: # B0 -> N1 white; send white home
							desired_moves += 1
							black_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								black_chose_desired_move += 1
						if new_B1 == B1 + 1 and new_N2 == N2 - 2 and new_W0 == W0 + 1: # B1 -> N2 white; send white home
							desired_moves += 1
							black_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								black_chose_desired_move += 1		
						if new_N1 == N1 + 1 and new_N3 == N3 - 2 and new_W0 == W0 + 1: # N1 -> N3 white; send white home
							desired_moves += 1
							black_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								black_chose_desired_move += 1		
						if new_N2 == N2 + 1 and new_N4 == N4 - 2 and new_W0 == W0 + 1: # N2 -> N4 white; send white home
							desired_moves += 1
							black_desired_moves += 1
							if move_num == i + 1:
								chose_desired_move += 1
								black_chose_desired_move += 1	
							
					'''						
							
		
		if move_num == 1:
			num_choose_one += 1
		if move_num == 2: 
			num_choose_two += 1
		move_choice = choose_move(move_num, moves) # choose the desired move 
		current_board = move_choice # change the current board to the new board according to move choice

		# player win condition 

		if current_board[0,2] == 2:
			num_white_wins += 1
			break
		if current_board[2,2] == -2:
			num_black_wins += 1
			break

		current_player = change_player(current_player) # end turn and change players 

	num_total_games += 1
	if num_total_games % 5000 == 0:
		print("Games simulated:", num_total_games)

time_end = time.time()
time_taken = time_end - time_start

#print("Number of moves that the desired move was possible:", desired_moves)
#print("Number of moves where both options were desired moves:", two_desired_moves)
#print("Number of times that white had the desired move:", white_desired_moves)
#print("Number of times that black had the desired move:", black_desired_moves)
#print("Number of times that white chose the desired move:", white_chose_desired_move)
#print("Number of times that black chose the desired move:", black_chose_desired_move)
#print("Number of times that the desired move was chosen:", chose_desired_move)
#print("Number of turns with one possible move:", num_one_moves)
#print("Number of turns with two possible moves:", num_two_moves)
#print("Number of turns chosen move one:", num_choose_one)
#print("Number of turns chosen move two:", num_choose_two)
print("Total time taken: {:.2f} seconds" .format(time_taken))
print("Games per minute: {:.0f}" .format(num_total_games / time_taken * 60))
print("Games per hour {:.0f}" .format(num_total_games / time_taken * 60 * 60))
#print("Number of times 0 was rolled:", num_zeros)
#print("Number of times 1 was rolled:", num_ones)
#print("Number of times 2 was rolled:", num_twos)
print("Average number of turns per game:", int(sum([num_zeros, num_ones, num_twos]) / num_total_games))
print("Number of times black starts:", num_black_starts)
print("Number of times white starts:", num_white_starts)
print("Number of black wins:", num_black_wins)
print("Number of white wins:", num_white_wins)
print("Percent black wins: {:.2f}%" .format(num_black_wins / num_total_games * 100))
print("Percent white wins: {:.2f}%" .format(num_white_wins / num_total_games * 100))
print()
print("Thank you for playing!")