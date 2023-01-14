from pyfiglet import figlet_format
def greeting():
    return figlet_format("Welcome to tic tac toe", font= "banner")


player1_name = input("player one insert your name: ")
player2_name = input("player two insert your name: ")
def name_insert():
    return f"Hello {player1_name} and {player2_name}"


def XorO():
    print(f"{player1_name} is playing with X\n {player2_name} is playing with O")


def switch_player():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"