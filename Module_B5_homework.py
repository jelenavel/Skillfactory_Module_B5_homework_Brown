board = [["-", "-","-"],
		["-", "-","-"],
		["-", "-","-"]]
def display():
	print("  0 1 2")
	for count, row in enumerate(board):
		print(count, *row)

def win_vertically(board):
    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != "-":
                print(f"Player {check[0]} is the winner vertically")
                return True

def win_gorizontally(board):
    for row in board:
        for cell in row:
            if row.count(row[0]) == len(row) and row[0] != "-":
                print(f"Player {row[0]} is the winner gorizontally")
                return True

def win_diagonally_down(board):
	diags = []
	for x in range(len(board)):
		diags.append(board[x][x])
	if diags.count(diags[0]) == len(diags) and diags[0] != "-":
		print(f"Player {diags[0]} is the winner diagonally")
		return True

def win_diagonally_up(board):
	diags = []
	for col, row in enumerate(reversed(range(len(board)))):
		diags.append(board[row][col])
	if diags.count(diags[0]) == len(diags) and diags[0] != "-":
		print(f"Player {diags[0]} is the winner diagonally")
		return True

# Player_x
def player_x():
	play = True
	while play:
		column_choice = int(input("You are playing 'x'.What column do you want to play?(0,1,2): "))
		while column_choice not in range(0,3):
			print("Wrong input.Try again")
			column_choice = int(input("What column do you want to play?(0,1,2): "))
		else:
			row_choice = int(input("What row do you want to play?(0,1,2): "))
			while row_choice not in range(0, 3):
				print("Wrong input.Try again")
				row_choice = int(input("What row do you want to play?(0,1,2): "))
			else:
				if board[row_choice][column_choice] != "-":
					print("This position is played.Choose another one!")
				else:
					board[row_choice][column_choice] = "x"
					play = False

# Player_0
def player_0():
	play = True
	while play:
		column_choice = int(input("You are playing '0'.What column do you want to play?(0,1,2): "))
		while column_choice not in range(0, 3):
			print("Wrong input.Try again")
			column_choice = int(input("What column do you want to play?(0,1,2): "))
		else:
			row_choice = int(input("What row do you want to play?(0,1,2): "))
			while row_choice not in range(0, 3):
				print("Wrong input.Try again")
				row_choice = int(input("What row do you want to play?(0,1,2): "))
			else:
				if board[row_choice][column_choice] != "-":
					print("This position is played.Choose another one!")
				else:
					board[row_choice][column_choice] = "0"
					play = False


no_win = True
while no_win:
	display()
	player_x()
	display()
	if (win_vertically(board) or win_gorizontally(board)) or (win_diagonally_down(board) or win_diagonally_up(board)):
		print("Game is over")
		no_win = False
	else:
		player_0()
		if (win_vertically(board) or win_gorizontally(board)) or (win_diagonally_down(board) or win_diagonally_up(board)):
			display()
			print("Game is over")
			no_win = False









