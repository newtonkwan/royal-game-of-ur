# Run this file to for player vs player in 3x4, no flower, 0-2 die Ur 

from game_logic import init_board, game_rules, roll_die, possible_moves, first_player, choose_move, current_player_info, show_possible_moves, current_board_info, current_die_info, choose_move_num, choose_move, change_player, play_again, player_win, game_mode_info
import time

game_mode = 'player_vs_player'
game_rules() # shows the game rules
game_mode_info(game_mode) # welcome 
board = init_board() # initialize the board 
first = first_player() # initialize first player; will be 'b' or 'w'

current_board = board # current board 
current_player = first # current player 
print("Game Start!")
time.sleep(1)

while True:

	current_player_info(current_player) # show current player info 
	current_board_info(current_board) # show current board info
	input("Press Enter to roll")
	time.sleep(1)
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
		current_player = change_player(current_player)
		time.sleep(1.75)
		continue

	time.sleep(1.25)
	show_possible_moves(moves) # show possible moves 
	move_num = choose_move_num(moves) # choose the move number 
	move_choice = choose_move(move_num, moves) # choose the desired move 
	current_board = move_choice # change the current board to the new board according to move choice
	time.sleep(1.75)
	print("--------------------------------")

	# player win condition 

	win_condition = player_win(current_board)
	if win_condition == True:
		break

	current_player = change_player(current_player) # end turn and change players 

play_again(game_mode)




