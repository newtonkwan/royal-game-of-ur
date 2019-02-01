# execute this file to play the game 

from game_logic import init_board, game_rules

game_rules()
board = init_board() # initialize the board 
first_player = input("Who goes first? (Enter b / w): ")
print(board)
