# Computer vs Computer
# an arena to match up computer agents in 3x4, no flower, 0-2 die Ur. 

from game_logic import init_board, game_rules, roll_die, possible_moves, first_player, choose_move, current_player_info, show_possible_moves, current_board_info, current_die_info, choose_move_num, choose_move, change_player, player_choose_color, play_again, player_win, choose_two_computer_agents
import basic_one
import basic_two
import basic_three
import basic_four
import random 
import time


game_rules()

# initialize generally important game metrics 

num_black_wins = 0 # number of black wins 
num_white_wins = 0 # number of white wins 
num_black_starts = 0 # number of times black starts 
num_white_starts = 0 # number of times white starts 
num_zeros = 0 # number of zeros rolled 
num_ones = 0 # number of ones rolled 
num_twos = 0 # number of twos rolled 
num_total_games = 0 # number of total games played

# specific testing game metrics 
num_one_moves = 0 # number of times one move is available
num_two_moves = 0 # number of times two moves are available
num_no_pref_move = 0 # number of moves in strategy_move_nums with no preferred moves 
num_one_pref1_move = 0 # number of moves in strategy_move_nums with one move and it is the preference_one move
num_one_pref2_move = 0 # number of moves in strategy_move_nums with one move and it is the preference_two_move
num_two_pref2_moves = 0 # number of moves in strategy_move_nums with two moves and they are both preference_two_moves
num_one_pref1_one_pref2_moves = 0 # number of moves in strategy_move_nums with two moves and one is pref_one and one is pref_two

# select agents 
agent_1_dict, agent_2_dict = choose_two_computer_agents() # dictionaries Ex. {"b": "Random"}, {"w":"BasicOne"}

#agent_1_dict, agent_2_dict = {"b" : "BasicFour"}, {"w" : "BasicThree"}
# agent information
agent_one_color = list(agent_1_dict.keys())[0]# agent one will always be black 
agent_one = list(agent_1_dict.values())[0] 
agent_two_color = list(agent_2_dict.keys())[0] # agent two will always be white
agent_two = list(agent_2_dict.values())[0] 

print("---------------------------------------------")
print("Computer (", agent_one, ")" " vs. Computer (", agent_two, ") Mode", sep = '')
print("---------------------------------------------")
print(agent_one, ": ", agent_one_color, sep = '')
print(agent_two, ": ", agent_two_color, sep = '')
print("--------------------------------------------------------")


while True:
	try: 
		num_games = int(input("How many games do you want to simulate? (Enter a number):"))
		break
	except ValueError:
		print("Oops. Invalid input. Try again")
print("Simulating", num_games, "games...")
half_games = num_games / 2 # half the total of num_games to be used for keeping track of who goes first
print()

time_start = time.time()
for i in range(num_games):
	board = init_board() # initialize the board 
	
	# Determine who goes first 

	# Uncomment to make Black go first
	#first = 'b'

	# Uncomment to make White go first
	#first = 'w'

	# Uncomment to have each go first an equal number of times 
	
	if num_white_starts != half_games:
		first = 'w'
	else:
		first = 'b'

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

		
		# Testing statistic
		# number of possible moves 
		if len(moves) == 1:
			num_one_moves += 1
		if len(moves) == 2:
			num_two_moves += 1
		
		# Choose strategy based on the agent 
		
		if current_player == "b":
			# Random
			if agent_1_dict[current_player] == "Random":
				move_num = random.choice(range(len(moves))) + 1
			# BasicOne
			if agent_1_dict[current_player] == "BasicOne":
				move_num = basic_one.choose_move_num(current_board, current_player, moves, current_roll)
			# BasicTwo 
			if agent_1_dict[current_player] == "BasicTwo":
				move_num = basic_two.choose_move_num(current_board, current_player, moves, current_roll)[0]
			# BasicThree
			if agent_1_dict[current_player] == "BasicThree":
				what_move  = basic_three.choose_move_num(current_board, current_player, moves, current_roll)
				move_num = what_move[0]		
			# BasicFour
			if agent_1_dict[current_player] == "BasicFour":
				what_move  = basic_four.choose_move_num(current_board, current_player, moves, current_roll)
				move_num = what_move[0]		


		if current_player == "w":
			# Random
			if agent_2_dict[current_player] == 'Random':
				move_num = random.choice(range(len(moves))) + 1
			# BasicOne
			if agent_2_dict[current_player] == "BasicOne":
				move_num = basic_one.choose_move_num(current_board, current_player, moves, current_roll)
			# BasicTwo 
			if agent_2_dict[current_player] == "BasicTwo":
				move_num = basic_two.choose_move_num(current_board, current_player, moves, current_roll)[0]
			# BasicThree
			if agent_2_dict[current_player] == "BasicThree":
				what_move  = basic_three.choose_move_num(current_board, current_player, moves, current_roll)
				move_num = what_move[0]		
			# BasicFour
			if agent_2_dict[current_player] == "BasicFour":
				what_move  = basic_four.choose_move_num(current_board, current_player, moves, current_roll)
				move_num = what_move[0]		

		'''
		# tests for BasicFour specific testings 
		move_num = what_move[0]
		no_pref_move = what_move[1]
		one_pref1_move = what_move[2]
		one_pref2_move = what_move[3]
		two_pref2_moves = what_move[4]
		one_pref1_one_pref2_moves = what_move[5]
		
		if no_pref_move == True:
			num_no_pref_move += 1
		if one_pref1_move == True:
			num_one_pref1_move += 1
		if one_pref2_move == True:
			num_one_pref2_move += 1
		if two_pref2_moves == True:
			num_two_pref2_moves += 1
		if one_pref1_one_pref2_moves == True:
			num_one_pref1_one_pref2_moves += 1

		'''
					
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

'''
# BasicFour testing game statistics 
num_turns_with_poss_moves = num_one_moves + num_two_moves
num_turns_with_pref_moves = num_one_pref1_move + num_one_pref2_move + num_two_pref2_moves + num_one_pref1_one_pref2_moves
print("BasicThree game statistics")
print("--------------------------")
print("Number of turns with possible moves:", num_turns_with_poss_moves)
print("Number of turns with no possible preference moves:", num_no_pref_move)
print("Number of turns with at least one preference moves:", num_turns_with_pref_moves)
print("Percent turns with no preference moves: {:.2f}%" .format(num_no_pref_move / num_turns_with_poss_moves * 100))
print("Percent turns with preference moves: {:.2f}%" .format(num_turns_with_pref_moves / num_turns_with_poss_moves * 100))
print("Percent turns choosing preference one moves: {:.2f}%" .format((num_one_pref1_move + num_one_pref1_one_pref2_moves) / num_turns_with_poss_moves *100))
print("Percent turns choosing preference two moves: {:.2f}%" .format((num_one_pref2_move + num_two_pref2_moves) / num_turns_with_poss_moves *100))
print("Number of turns with at least one possible preference one move:", num_one_pref1_move )
print("Number of turns with at least one possible preference two move:", num_one_pref2_move + num_two_pref2_moves + num_one_pref1_one_pref2_moves)
print("Number of turns with one possible preference one moves:", num_one_pref1_move)
print("Number of turns with one possible preference two moves:", num_one_pref2_move)
print("Number of turns with two possible preference two moves:", num_two_pref2_moves)
print("Number of turns with one possible preference one and one possible preference two moves:", num_one_pref1_one_pref2_moves)
print("Number of missing moves:", num_one_moves + num_two_moves - num_no_pref_move - num_one_pref1_move - num_one_pref2_move - num_two_pref2_moves - num_one_pref1_one_pref2_moves)
'''

# general game statistics 
print()
print("Game statistics")
print("---------------")
print("Total time taken: {:.2f} seconds" .format(time_taken))
print("Games per minute: {:.0f}" .format(num_total_games / time_taken * 60))
print("Games per hour {:.0f}" .format(num_total_games / time_taken * 60 * 60))
print("Average number of turns per game:", int(sum([num_zeros, num_ones, num_twos]) / num_total_games))
print("Number of times black starts:", num_black_starts)
print("Number of times white starts:", num_white_starts)
print("Number of black wins:", num_black_wins)
print("Number of white wins:", num_white_wins)
print("Percent black wins: {:.2f}%" .format(num_black_wins / num_total_games * 100))
print("Percent white wins: {:.2f}%" .format(num_white_wins / num_total_games * 100))
print()
print("Thank you for playing!")