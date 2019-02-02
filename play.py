# execute this file to play the game 

from game_logic import init_board, game_rules, roll_die, possible_moves
import pandas as pd

game_rules()
board = init_board() # initialize the board 
board[0,0] = 1
board[1,0] = 1
board[1,1] = 1
board[1,2] = 1
board[1,3] = -1
df = pd.DataFrame(board)
print("Current board")
print(df)

x = possible_moves("w", board, roll = 1)

for i in range(len(x)):
	print()
	df = pd.DataFrame(x[i])
	print("Possible move", i+1)
	print(df)
