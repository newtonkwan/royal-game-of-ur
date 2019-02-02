# execute this file to play the game 

from game_logic import init_board, game_rules, roll_die, possible_moves, first_player, choose_move, current_player_info, show_possible_moves, current_board_info, current_die_info, choose_move_num, choose_move

game_rules()
board = init_board() # initialize the board 
first = first_player() # initialize first player; will be 'b' or 'w'

current_board = board # current board 
current_player = first # current player 

while True:

	current_player_info(current_player) # show current player info 
	current_board_info(current_board) # show current board info

	input("Press Enter to roll")
	current_roll = roll_die() # roll die 
	current_die_info(current_roll) # show current die info

	# roll a 0 
	if current_roll == 0: 
		print("--------------------------------")
		if current_player == "w":
			current_player = 'b'
			continue
		if current_player == "b":
			current_player = 'w'
			continue
	
	moves = possible_moves(current_player, current_board, current_roll) # gets possible moves 
	# no possible moves 
	if len(moves) == 0: 
		print("No possible moves!")
		if current_player == "w":
			current_player = 'b'
			continue
		if current_player == "b":
			current_player = 'w'
			continue

	show_possible_moves(moves) # show possible moves 
	move_num = choose_move_num(moves) # choose the move number 
	move_choice = choose_move(move_num, moves) # choose the desired move 
	current_board = move_choice # change the current board to the new board according to move choice
	print("--------------------------------")

	# player win condition 

	if current_board[0,2] == 2:
		print(current_board)
		print("White has won the game!")
		break
	if current_board[2,2] == -2:
		print(current_board)
		print("Black has won the game!")
		break


	if current_player == "b":
		current_player = "w"
		continue
	if current_player == "w":
		current_player = "b"
		continue
		

print("Thank you for playing!")




