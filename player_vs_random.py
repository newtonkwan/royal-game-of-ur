# Run this file to to play against a randomly playing agent in 3x4, no flower, 0-2 die Ur 

from game_logic import init_board, game_rules, roll_die, possible_moves, first_player, choose_move, current_player_info, show_possible_moves, current_board_info, current_die_info, choose_move_num, choose_move, change_player, player_choose_color, play_again, player_win
import random 
import time

game_mode = 'player_vs_random'
game_rules()
print("--------------------------------")
print("Player vs. Computer Mode")
print("The agent you will be playing plays randomly.")
player = player_choose_color() # will be 'b' or 'w'
if player == 'b':
	computer = 'w'
if player == 'w':
	computer = 'b'
print("Player:", player)
print("Computer:", computer)

board = init_board() # initialize the board 
first = first_player() # initialize first player; will be 'b' or 'w'

current_board = board # current board 
current_player = first # current player 
print("Game Start!")
time.sleep(1)
print()

while True:

	current_player_info(current_player) # show current player info 
	current_board_info(current_board) # show current board info
	if current_player == player:
		input("Press Enter to roll")
		time.sleep(1)
	if current_player == computer:
		time.sleep(2)
	current_roll = roll_die() # roll die 
	current_die_info(current_roll) # show current die info

	# roll a 0 
	if current_roll == 0: 
		print("--------------------------------")
		current_player = change_player(current_player)
		time.sleep(1.75) # adds delay
		continue
	
	moves = possible_moves(current_player, current_board, current_roll) # gets possible moves 

	# no possible moves 
	if len(moves) == 0: 
		print("No possible moves!")
		print("--------------------------------")
		current_player = change_player(current_player)
		time.sleep(1.75)
		continue

	if current_player == player:
		time.sleep(1.5)
		show_possible_moves(moves) # show possible moves 
		time.sleep(0.75)
		move_num = choose_move_num(moves) # choose the move number 
	if current_player == computer:
		time.sleep(1)
		move_num = random.choice(range(len(moves))) + 1 # choose the move number. + 1 b/c human input 1 -> 0 for machine
	move_choice = choose_move(move_num, moves) # choose the desired move 
	current_board = move_choice # change the current board to the new board according to move choice
	time.sleep(2)
	if current_player == player:
		print("--------------------------------")

	# player win condition 

	win_condition = player_win(current_board)
	if win_condition == True:
		break

	current_player = change_player(current_player) # end turn and change players 

print("Thank you for playing!")
play_again(game_mode)



