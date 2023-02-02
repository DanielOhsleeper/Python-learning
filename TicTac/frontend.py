def greeting():
    print("Welcome to Tic Tac Toe")

def insert_names(state):
    user1 = input("Insert your name: ")
    user2 = input("Insert you name: ")
    state["user1"] = user1
    state["user2"] = user2

def check_move_input(move: str, state):
    move_list = move.split(" ")
    if len(move_list) == 2 and move_list[0].isdigit() and move_list[1].isdigit():
        move_tuple = int(move_list[0]), int(move_list[1])
        if 1 <= move_tuple[0] <= state["size"] and 1 <= move_tuple[1] <= state["size"]:
            return move_tuple
        else:
            return False
    else:
        return False


def update_board(state):
    user_inp = input("Choose your move by 2 numbers with space between: ").strip()
    is_valid_move = check_move_input(user_inp, state)
    while not is_valid_move:
        user_inp = input("Invalid input, try again: ")
        is_valid_move = check_move_input(user_inp, state)
    if state["board"][is_valid_move[0]-1][is_valid_move[1]-1] == "-":
        state["board"][is_valid_move[0]-1][is_valid_move[1]-1] = state["current_player"]



def print_board(state):
    for row_col in state["board"]:
        for place in row_col:
            print(place, end=" ")
        print()


def update_with_turn(state):
    if state["current_player"] == "X":
        state["current_player"] = "O"
    else:
        state["current_player"] = "X"


def winner_print(state):
    if state["current_player"] == "X":
        print(f"Congratulations {state['user1']} wins!")
    elif state["current_player"] == "O":
        print(f"Congratulations {state['user2']} wins!")



