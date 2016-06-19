def move_input():
    print("move (x1,y1) to (x2,y2):")
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    return (x1, y1), (x2, y2)


def h_turn(player):
    print("Turn: Player ", player)
    move = move_input()
    print(move)
    # verifier que le coup est possible
    return False


def c_turn(player):
    print("Turn: Computer ", player)
    # calcule le coup a faire
    return False


def hh_game():
    finish = True
    player = 1
    while finish:
        h_turn(player)
        player = -player  # swap player turn
        finish = False


def cc_game():
    finish = True
    player = 1
    while finish:
        c_turn(player)
        player = -player  # swap player turn
        finish = False
    return False


def hc_game():
    finish = True
    h_is = 1
    player = 1
    while finish:
        if h_is == player:
            finish = h_turn(player)
        else:
            finish = c_turn(player)
        player = -player  # swap player turn
    return False


def new_game(game_type):
    if game_type == 0:
        print("Human vs Computer: The game can start")
    elif game_type == 2:
        print("Computer vs Computer: The game can start")
    elif game_type == 1:
        print("Human vs Human: The game can start")
        hh_game()
