# functions used to play the royal game of ur 

import numpy as np


def init_board():
	board = np.zeros((3,4))
	board[0,1] = 2
	board[2,1] = -2 
	return board

def game_rules():
	print("Welcome to the Royal Game of Ur!")
	print("--------------------------------")
	print("How to Play")
	print("This is a two-person race to the finish.")
	print("Players will take turns rolling a die and moving their pieces.")
	print("Black pieces are labelled as positive and white pieces are labelled negative")
	print("Ex: 2 = two black pieces on the tile; -1 = one black piece on the tile; 0 = no pieces on tile")
	input("Press Enter to start the game!")

