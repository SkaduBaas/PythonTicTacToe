# Milestone Project 1 -- Tic Tac Toe Game
#from IPython.display import clear_output
import random
def show_board(board):
	#clear_output() #Optional
	print("\n "+ board[7] +" | "+ board[8] +" | "+ board[9])
	print("-----------")
	print(" "+ board[4] +" | "+ board[5] +" | "+ board[6])
	print("-----------")
	print(" "+ board[1] +" | "+ board[2] +" | "+ board[3] +"\n")
	
'''def player_input():
	token = "insert"
	while(len(token) >= 2):
		print("Whose turn is it?")
		token = input("X or O? -> ")
		if(token == 'X' or token == 'O'):
			print("Choose where you want to put your token!")
			spot = int(input("#? -> "))
		else:
			print("Sorry, try again.")
			token = "nope"
			continue	
	marker = {'spot': spot, 'token': token.upper()}
	return marker'''

def assign_player():
	marker = ' '
	while not (marker == 'X' or marker == 'O'):
		marker = input("Player 1: Do you want to be X or O?").upper()
	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')

def put_it_there(board, marker, position):
	board[position] = marker

def who_goes_first():
	if random.randint(0, 1) == 0:
		return "Player 2"
	else:
		return "Player 1"

def is_full(board):
	for x in range(1,10):
		if already_used(board, x): #also: if ' ' in board[1:]:
			return False
	return True

def already_used(board, position):
	return board[position] == ' '

def we_have_a_winner(board, marker):
	if(board[7] == board[8] == board[9] == marker):
		return True
	elif(board[4] == board[5] == board[6] == marker):
		return True
	elif(board[1] == board[2] == board[3] == marker):
		return True
	elif(board[7] == board[4] == board[1] == marker):
		return True
	elif(board[8] == board[5] == board[2] == marker):
		return True
	elif(board[9] == board[6] == board[3] == marker):
		return True
	elif(board[7] == board[5] == board[3] == marker):
		return True
	elif(board[9] == board[5] == board[1] == marker):
		return True
	else:
		return False

def choose_next(board):
	position = 0
	while position not in range(1,10) or not already_used(board, position):
		position = int(input("Choose your next position: (1-9) "))
	return position

def go_again():
	return input("Do you want to play again? Yes or No: ").lower().startswith('y')


print("\nTIME FOR TIC-TAC-TOE!\n")

while True:
	board = [' '] * 10
	P1_token, P2_token = assign_player()
	turn = who_goes_first()
	print(turn +" will go first.")
	playing_now = True
	
	while playing_now:
		if turn == "Player 1":
			show_board(board)
			position = choose_next(board)
			put_it_there(board, P1_token, position)
			if we_have_a_winner(board, P1_token):
				show_board(board)
				print("Congrats! You won, Player 1!")
				playing_now = False
			else:
				if is_full(board):
					show_board(board)
					print("Aww a tie? Too bad.")
					break
				else:
					turn = "Player 2"
		else:
			show_board(board)
			position = choose_next(board)
			put_it_there(board, P2_token, position)
			if we_have_a_winner(board, P2_token):
				show_board(board)
				print("Congrats! You won, Player 2!")
				playing_now = False
			else:
				if is_full(board):
					show_board(board)
					print("Aww a tie? Too bad.")
					break
				else:
					turn = "Player 1"
	if not go_again():
		break