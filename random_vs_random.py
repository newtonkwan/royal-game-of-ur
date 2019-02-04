# execute this file to see two agents play randomly against each other

from game_logic import init_board, game_rules, roll_die, possible_moves, first_player, choose_move, current_player_info, show_possible_moves, current_board_info, current_die_info, choose_move_num, choose_move, change_player
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

print("You simulating two computers play against each other")
print("Random vs Random")
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
	if num_white_starts != half_games:
		first = 'w'
	else:
		first = 'b'
	#first = random.choice(['b', 'w']) # initialize first player; will be 'b' or 'w'
	#first = 'b'
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

		move_num = random.choice(range(len(moves))) + 1 # choose the move number. + 1 b/c human input 1 -> 0 for machine
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

#print("Number of turns with one possible move:", num_one_moves)
#print("Number of turns with two possible moves:", num_two_moves)
#print("Number of turns chosen move one:", num_choose_one)
#print("Number of turns chosen move two:", num_choose_two)
print("Total time taken: {:.2f} seconds" .format(time_taken))
print("Games per minute: {:.0f}" .format(num_total_games / time_taken * 60))
#print("Number of times 0 was rolled:", num_zeros)
#print("Number of times 1 was rolled:", num_ones)
#print("Number of times 2 was rolled:", num_twos)
print("Average number of moves per game:", int(sum([num_zeros, num_ones, num_twos]) / num_total_games))
print("Number of times black starts:", num_black_starts)
print("Number of times white starts:", num_white_starts)
print("Number of black wins:", num_black_wins)
print("Number of white wins:", num_white_wins)
print("Percent black wins: {:.2f}%" .format(num_black_wins / num_total_games * 100))
print("Percent white wins: {:.2f}%" .format(num_white_wins / num_total_games * 100))
print()
print("Thank you for playing!")