

if __name__ == "__main__":
    print(greeting())
    print(name_insert())
    XorO()
    while gameRunning:
        printBoard(board)
        playerInput(board)
        game_stuck(board)
        switch_player()
        get_winner()