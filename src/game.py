def move_input():
    print("move (x1,y1) to (x2,y2):")
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    return (x1, y1), (x2, y2)


def hh_game():
    finish = True
    while finish:
        print("Turn: Player 1")
        move = move_input()
        print(move)
        finish = False


def new_game(game_type):
    if game_type == 0:
        print("Human vs Computer: The game can start")
    elif game_type == 2:
        print("Computer vs Computer: The game can start")
    elif game_type == 1:
        print("Human vs Human: The game can start")
        hh_game()
