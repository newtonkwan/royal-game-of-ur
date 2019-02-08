# functions used to play the royal game of ur 

import numpy as np
import pandas as pd
import time

def assign_agents(agent_one, agent_two):
	# assign agents their colors 
	agents = []
	if agent_one == 'Random':
		random_agent_p1 = 'b'
		if agent_two == 'Random':
			random_agent_p2 = 'w'
		if agent_two == 'BasicOne':
			basicOne_p2 = 'w'
		if agent_two == 'BasicTwo':
			basicTwo_p2 = 'w'
		if agent_two == 'BasicThree':
			basicThree_p2 = 'w'
	if agent_one == 'BasicOne':
		basicOne_p1 = 'b'
		if agent_two == 'Random':
			random_agent_p2 = 'w'
		if agent_two == 'BasicOne':
			basicOne_p2 = 'w'
		if agent_two == 'BasicTwo':
			basicTwo_p2 = 'w'
		if agent_two == 'BasicThree':
			basicThree_p2 = 'w'	
	if agent_one == 'BasicTwo':
		basicTwo_p1 = 'b'
		if agent_two == 'Random':
			random_agent_p2 = 'w'
		if agent_two == 'BasicOne':
			basicOne_p2 = 'w'
		if agent_two == 'BasicTwo':
			basicTwo_p2 = 'w'
		if agent_two == 'BasicThree':
			basicThree_p2 = 'w'	
	if agent_one == 'BasicThree':
		basicThree_p1 = 'b'
		if agent_two == 'Random':
			random_agent_p2 = 'w'
		if agent_two == 'BasicOne':
			basicOne_p2 = 'w'
		if agent_two == 'BasicTwo':
			basicTwo_p2 = 'w'
		if agent_two == 'BasicThree':
			basicThree_p2 = 'w'	
	return random_agent_p1, random_agent_p2, basicOne_p1, basicOne_p2, basicTwo_p1, basicTwo_p2, basicThree_p1, 

def change_player(player):
	# switch players when the turn is over 
	if player == 'w':
		new_player = 'b'
		return new_player
	if player == 'b':
		new_player = 'w'
		return new_player

def choose_agent():
	# choose the agent that you want to play against in player vs computer 
	print()
	print("Agents available:")
	print("")
	print("Random")
	print("BasicOne")
	print("BasicTwo")
	print("BasicThree")
	print()
	while True:
		try: 
			agent = input("What agent would you like to face? (Enter agent name): ")
			if agent == 'random' or agent == 'Random': 
				break
			if agent == 'basicone' or agent == "basicOne" or agent == "BasicOne":
				break
			if agent == 'basictwo' or agent == "basicTwo" or agent == "BasicTwo":
				break
			if agent == 'basicthree' or agent == "basicThree" or agent == "BasicThree":
				break
			if agent != 'random' or agent != 'Random' or agent != 'basicone' or agent != "basicOne" or agent != "BasicOne" or agent != 'basictwo' or agent != "basicTwo" or agent != "BasicTwo" or agent != 'basicthree' or agent != 'basicTwo' or agent != 'BasicThree':
				print("Oops! Invalid command. Try again")
		except ValueError:
			print("Oops! Invalid command. Try again")
	return agent

def choose_two_computer_agents():
	# choosing agents to play in computer vs. computer v2
	print()
	print("Agents available:")
	print("")
	print("Random")
	print("BasicOne")
	print("BasicTwo")
	print("BasicThree")
	print("BasicFour")
	print()
	agent_1_dict = {}
	agent_2_dict = {}
	while True:
		try: 
			agent_one = input("Choose the first agent (Enter agent name): ")
			if agent_one == 'random' or agent_one == 'Random': 
				agent_1_dict['b'] = "Random"
				break
			if agent_one == 'basicone' or agent_one == "basicOne" or agent_one == "BasicOne":
				agent_1_dict['b'] = "BasicOne"
				break
			if agent_one == 'basictwo' or agent_one == "basicTwo" or agent_one == "BasicTwo":
				agent_1_dict['b'] = "BasicTwo"
				break
			if agent_one == 'basicthree' or agent_one == "basicThree" or agent_one == "BasicThree":
				agent_1_dict['b'] = "BasicThree"
				break
			if agent_one == 'basicfour' or agent_one == "basicFour" or agent_one == "BasicFour":
				agent_1_dict['b'] = "BasicFour"
				break
			if agent_one != 'random' or agent_one != 'Random' or agent_one != 'basicone' or agent_one != "basicOne" or agent_one != "BasicOne" or agent_one != 'basictwo' or agent_one != "basicTwo" or agent_one != "BasicTwo" or agent_one != 'basicthree' or agent_one != "basicThree" or agent_one != "BasicThree" or agent_one != 'basicfour' or agent_one != "basicFour" or agent_one != "BasicFour":
				print("Oops! Invalid command. Try again")
		except ValueError:
			print("Oops! Invalid command. Try again")

	while True:
		try: 
			agent_two = input("Choose the second agent (Enter agent name): ")
			if agent_two == 'random' or agent_two == 'Random': 
				agent_2_dict['w'] = "Random"
				break
			if agent_two == 'basicone' or agent_two == "basicOne" or agent_two == "BasicOne":
				agent_2_dict['w'] = "BasicOne"
				break
			if agent_two == 'basictwo' or agent_two == "basicTwo" or agent_two == "BasicTwo":
				agent_2_dict['w'] = "BasicTwo"
				break
			if agent_two == "basicthree" or agent_two == "basicThree" or agent_two == "BasicThree":
				agent_2_dict['w'] = "BasicThree"
				break
			if agent_two == 'basicfour' or agent_two == "basicFour" or agent_two == "BasicFour":
				agent_2_dict['w'] = "BasicFour"
				break
			if agent_two != 'random' or agent_two != 'Random' or agent_two != 'basicone' or agent_two != "basicOne" or agent_two != "BasicOne" or agent_two != 'basictwo' or agent_two != "basicTwo" or agent_two != "BasicTwo" or agent_two != 'basicthree' or agent_two != "basicThree" or agent_two != "BasicThree" or agent_two != 'basicfour' or agent_two != "basicFour" or agent_two != "BasicFour":
				print("Oops! Invalid command. Try again")
		except ValueError:
			print("Oops! Invalid command. Try again")
	return agent_1_dict, agent_2_dict


def choose_move(move_num, moves):
	# chooses the move based on the move number 
	move = moves[move_num - 1]
	return move

def choose_move_num(moves):
	# returns the chosen move number 
	# input: move number
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

def computer_choose_color(player):
	# assigns the computer the color not chosen by the player 
	if player == 'b':
		computer = 'w'
	if player == 'w':
		computer = 'b'
	return computer

def current_board_info(board):
	# displays the current board nicely 
	df_board = pd.DataFrame(board, index = ["", "", ""] ) 
	print()
	print(df_board.to_string(header=False)) # prints w/o col or index
	print()
	return 

def current_die_info(roll):
	# displays info about the current die roll 
	print("--------------------------------")
	if roll == 0:
		print("The roll is", roll, "... Bad Luck!")
	if roll != 0:
		print("The roll is ", roll)
		print("--------------------------------")
	return 

def current_player_info(player):
	# displays info about the current player
	if player == "w":
		print("It is White's turn!")
	if player == "b":
		print("It is Black's turn!")
	return 

def first_player():
	# returns the player that will start the game 
	# inputs only 'b' or 'w'
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

def game_mode_chosen(agent):
	# returns the game mode based off of the agent chose
	if agent == 'random' or agent == 'Random':
		game_mode = 'player_vs_random'
	if agent == 'basicone' or agent == "basicOne" or agent == "BasicOne":
		game_mode = 'player_vs_basic1'
	if agent == 'basictwo' or agent == "basicTwo" or agent == "BasicTwo":
		game_mode = 'player_vs_basic2'
	if agent == 'basicthree' or agent == "basicThree" or agent == "BasicThree":
		game_mode = 'player_vs_basic3'
	return game_mode

def game_mode_info(game_mode):
	# displays the game mode info 
	if game_mode == 'player_vs_player':
		print("--------------------------------")
		print("Player vs. Player")
	if game_mode == 'player_vs_random':
		print("--------------------------------")
		print("Player vs. Computer (Random) Mode")
		print("The agent you will be playing plays randomly.")
	if game_mode == 'player_vs_basic1':
		print("--------------------------------")
		print("Player vs. Computer (BasicOne) Mode")
		print("The agent you will be playing uses BasicOne strategy.")		
	if game_mode == 'player_vs_basic2':
		print("--------------------------------")
		print("Player vs. Computer (BasicTwo) Mode")
		print("The agent you will be playing uses BasicTwo strategy.")	
	return

def game_rules():
	# the introduction when the game is started that explains the rules 
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
	x = [["W1", "W0", "W3", "W2"],["N1", "N2", "N3", "N4"], ["B1", "B0", "B3", "B2"] ]
	df_board = pd.DataFrame(x, index = ["", "", ""] ) 
	print()
	print(df_board.to_string(header=False)) # prints w/o col or index
	print()
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

def init_board():
	# initializes the board 
	board = np.zeros((3,4), dtype = np.int8)
	board[0,1] = 2
	board[2,1] = -2 
	return board

def play_again(game_mode):
	# asks if the player would like to play again 
	print("Thank you for playing!")
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
		if game_mode == 'player_vs_player':
			exec(open('player_vs_player.py').read())
	return

def player_choose_color():
	# allows the player to choose what color he'd like to be
	print("-------------------------------------------------")
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

def player_info(player_one, player_two, game_mode):
	# displays what colors of the two players are 
	print("-------------------------------------------------")
	if game_mode == 'player_vs_random' or game_mode == 'player_vs_basic1' or game_mode == 'player_vs_basic2':
		if player_one == 'b':
			print("Player: Black")
			print("Computer: White")
		if player_one == 'w':
			print("Player: White")
			print("Computer: Black")	

	return

def player_win(board):
	# the win condition for each player 
	if board[0,2] == 2:
		print("White has won the game!")
		current_board_info(board)
		return True
	if board[2,2] == -2:
		print("Black has won the game!")
		current_board_info(board)
		return True
	return False

def possible_moves(player_turn, board, roll):
	# W1 W0 W3 W2
	# N1 N2 N3 N4
	# B1 B0 B3 B2

	# determines all possible moves given a board state and die roll 

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

def roll_die():
	# rolls the die 
	roll = int(np.random.randint(3, size = 1))
	return roll

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
	return









