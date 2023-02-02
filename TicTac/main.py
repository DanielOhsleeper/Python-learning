from frontend import greeting
from backend import run_game

if __name__ == '__main__':
    current_state = {
        "current_player": 'X',
        "board": [],
        "size": None,
        "user1": None,
        "user2": None
    }
    greeting()
    game = run_game(current_state)
    while game:
        current_state = {
            "current_player": 'X',
            "board": [],
            "size": None,
            "user1": None,
            "user2": None
        }
        game = run_game(current_state)
