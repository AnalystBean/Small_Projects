import random

# Tic Tac Toe board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_still_going = True

# Who won? or Tie?
winner = None

# Whose turn is it
current_player = "X"

# AI player
ai_player = "O"

# Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Play a game of tic tac toe
def play_game():

    # Display initial board
    display_board()

    while game_still_going:

        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # Check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()
    
    # The game is over
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

# Handle a single turn of an arbitrary player
def handle_turn(player):
    print(player + "'s turn.")
    position = None

    if player == "X":
        position = input("Choose a position from 1-9: ")
    elif player == "O":
        position = ai_move()

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player

    display_board()

def ai_move():
    # AI move
    # returns the best move for AI
    best_score = None
    best_move = None
    for i in range(0,9):
        if board[i] == "-":
            board[i] = ai_player
            score = minimax(board, 0, False)
            board[i] = "-"
            if best_score == None or score > best_score:
                best_score = score
                best_move = i
    return str(best_move + 1)

def minimax(board, depth, isMaximizing):
    result = check_if_game_over()
    if result != None:
        if result == ai_player:
            return 1
        elif result == "X":
            return -1
        elif result == "Tie":
            return 0
    if isMaximizing:
         best_score = -float("inf")
        for i in range(0, 9):
            if board[i] == "-":
                board[i] = ai_player
                score = minimax(board, depth + 1, False)
                board[i] = "-"
                best_score = max(score, best_score)
    else:
        best_score = float("inf")
        for i in range(0, 9):
            if board[i] == "-":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = "-"
                best_score = min(score, best_score)
    return best_score

def check_if_game_over():
    check_for_winner()
    check_if_tie()
    return winner

def check_for_winner():
    global winner
    # Check rows
    row_winner = check_rows()
    # Check columns
    column_winner = check_columns()
    # Check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return None

def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return None

def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return None

def check_if_