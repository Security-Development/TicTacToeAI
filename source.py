HUMAN = False
AI    = True

HUMAN_MARK = 1
AI_MARK    = -1

board = [
	0, 0, 0,
	0, 0, 0,
	0, 0, 0
]

def find_empty(board):
	return [ k for k, v in enumerate(board) if v == 0 ]

def is_win(board, player):
	win = [
	 [0, 1, 2],
	 [3, 4, 5],
	 [6, 7, 8],
	 [0, 3, 6],
	 [1, 4, 7],
	 [2, 5, 8],
	 [0, 4, 8],
	 [2, 4, 6]
	]

	for x, y, z in win:
		if (board[x] == board[y] == board[z]) and (board[x] == player):
			return True
	
	return False

def min_max(board, depth, turn):
	position = -1

	if depth == 0 or is_win(board, AI_MARK) or is_win(board, HUMAN_MARK):
		return -1, 1 if is_win(board, AI_MARK) else -1

	if turn == AI:
		value = -99999999999999999
		for i in find_empty(board):
			board[i] = AI_MARK
			_, score = min_max(board, depth - 1, HUMAN)
			board[i] = 0

			if score > value:
				position = i
				value = score

			if score == 1:
				break

	else:
		value = 99999999999999999

		for i in find_empty(board):
			board[i] = HUMAN_MARK
			_, score = min_max(board, depth - 1, AI)
			board[i] = 0

			if score < value:
				position = i
				value = score

			if score == -1:
				break

	return position, value

def view():
	global board
	for k, v in enumerate(board):
		if (k ) % 3 == 0:
			print()
		if v == 0:
			print("_ ", end="")
		elif v== 1:
			print("O ", end="")
		elif v== 2:
			print("X ", end="")


while find_empty(board):
	pos, _ = min_max(board, 9, AI)
	board[pos] = 1
	
	view()

	index = int(input("index > "))

	while 1:
		if index in find_empty(board):
			board[index] = 2
			break
		else:
			print("Cannot be duplicates")
			index = int(input("index > "))
