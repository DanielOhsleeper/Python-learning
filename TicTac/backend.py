from frontend import update_board, print_board, update_with_turn, winner_print, insert_names


def check_size_input(size: str):
    if size.isdigit() and 3 <= int(size) <= 9:
        return True
    return False



def board_size(state):
    n = input("Select board size between 3 and 9: ").strip()
    is_valid_size = check_size_input(n)
    while not is_valid_size:
        n = input("Wrong input. Try again: ").strip()
        is_valid_size = check_size_input(n)
    state["size"] = int(n)
    for row_num in range(state["size"]):
        state["board"].append([])
        for column_num in range(state["size"]):
            state["board"][row_num].append("-")



def get_row_winner(state):
    row_winnerX = ["X" for i in range(state["size"])]
    row_winnerO = ["O" for i in range(state["size"])]
    for row_list in state["board"]:
        if row_list == row_winnerX or row_list == row_winnerO:
            return True
    return False


def get_column_winner(state):
    count = 0
    for row in range(1, state["size"]+1):
        for col in range(1, state["size"]+1):
            if state["board"][col-1][row-1] == state["current_player"]:
                count += 1
        if count == state["size"]:
            return True
        count = 0
    return False


def get_diagonal_winner1(state):
    count = 0
    stat = []
    for num in range(1, state["size"]+1):
        if state["board"][num-1][num-1] == state["current_player"]:
            count += 1

    if count == state["size"]:
        return True
    return False

def get_diagonal_winner2(state):
    count = 0
    stat = []
    for num in range(1, state["size"] + 1):
        if state["board"][num - 1][state["size"] - num] == state["current_player"]:
            count += 1
    if count == state["size"]:
        return True
    return False

def get_winner(state):
    if get_row_winner(state) or get_column_winner(state) or get_diagonal_winner1(state) or get_diagonal_winner2(state):
        return True
    return False


def no_moves_left(state):
    count_list = []
    for row in state["board"]:
        count = row.count("-")
        if count == 0:
            count_list.append(count)
        if len(count_list) == state["size"]:
            print("The game is stuck")
            return True
    return False


def run_game(state):
    new_game = True
    while True:
        if new_game:
            insert_names(state)
            board_size(state)
            new_game = False
        update_board(state)
        print_board(state)
        if get_winner(state) or no_moves_left(state):
            winner_print(state)
            ask = input("End game, do you wanna play again?y/n")
            if "n" in ask:
                return False
            if "y" in ask:
                return True
        update_with_turn(state)

