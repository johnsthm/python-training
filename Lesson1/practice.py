# Tic Tac Toe Game

from random import randint

# Game Board
board = [0, 1, 2, 
		 3, 4, 5, 
		 6, 7, 8]

def print_board():
	''' Prints the Game Board to the command line

	'''
	for item in range(0, len(board)):
		if item % 3 == 0 and item != 0:
			print '|',
			print('\n---------')
		print '|' + str(board[item]),
	print '|',
	print('\n---------')

def check_line_for_win(character, pos1, pos2, pos3):
	# TODO: Check if this line is a winning line (all positions have 'character'). Return True if a winning line.

def check_for_winner(player):
	# Check if a winning row exists
	if check_line_for_win(player, 0, 1, 2):
		return True
	if check_line_for_win(player, 3, 4, 5):
		return True
	# TODO: put rest of tests for rows here

	# TODO: Check if a winning column exists
	
	# TODO: Check if a winning diagonal exists
		
def is_cats_game():
	# Return True if a Cat's Game happened (that is, the number_of_positions_left is 0)

def play_game():
	''' Start the game. This is the game's 'main' function 
	'''
	global number_of_positions_left
	number_of_positions_left = 9
	print("Welcome to tic-tac-toe!")
	while True: 
		# TODO: Ask the user for a position number (hint: use raw_input)

		# This occurs if the position is out of range
		if position > len(board) - 1:
			print('Position out of range.')
			continue

		if board[position] != 'x' and board[position] != 'o':
			# TODO: Change the text in the list (board) at this position to 'x'; this is x's turn. Also, this means that
			# there is one less position left on the board

			if check_for_winner('x'):
				# TODO: Print "=== X Won! ===" and print the board
				break
			if is_cats_game():
				# TODO: Let the player know it's a Cat's Game. Print the board.
				break

			while True:
				# TODO: Choose a random position for the opponent; set this value to the 
				# variable 'opponent_position'

				if board[opponent_position] != 'x' and board[opponent_position] != 'o':
					# TODO: Change the text in the list (board) at this position to 'o'; this is o's turn. Also, this means that
					# there is one less position left on the board
					break

			# Check if opponent won 
			if check_for_winner('o'):
				# TODO: Print "=== O Won! ===" and print the board
				break
			# Check for Cat's Game
			if is_cats_game():
				# TODO: Let the player know it's a Cat's Game. Print the board.
				break

		else:
			print('Spot taken; please select another spot.')

		print_board()

		# We reached the end of the while loop; now we go back to the top of the loop! (line 47)

# Start the game
play_game()