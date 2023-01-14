board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
winner = None
gameRunning = True
currentPlayer = "X"


def printBoard(board):

    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")


def playerInput(board):
    inp = int(input(f"Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp - 1] = currentPlayer
    else:
        print(f"Oops the spot is not empty!")


def get_row_winner(board):
    global winner
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] != "-":
        winner = board[6]
        return True


def get_column_winner(board):
    global winner
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] != "-":
        winner = board[2]
        return True


def get_diagonal_winner(board):
    global winner
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] != "-":
        winner = board[2]
        return True


def game_stuck(board):
    if "-" not in board:
        printBoard(board)
        print("Game is stuck!")
        gameRunning = False


def get_winner():
    if get_diagonal_winner(board) or get_column_winner(board) or get_row_winner(board) and "X" in winner:
        print(f"The winner is {player1_name}")

    elif get_diagonal_winner(board) or get_column_winner(board) or get_row_winner(board) and "O" in winner:
        print(f"The winner is {player2_name}")