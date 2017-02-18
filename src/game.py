# TODO: modify h_turn in order not to let player move if it's not a correct move
# TODO: allow h_player to be player 1 & c_player to be player -1

from src.gui import *
from src.ai import *
from src.pieces import *

player = -1
players = {}
ia_type = "viral"
difficulty = 3


def select_game_type():

    global players

    game_type = 1
    if game_type != -1:
        print("There is a shortcut for the test, game_type = ", game_type)

    while game_type < 0 or 2 < game_type:
        game_type = input("""What kind of game? (H:human, C: computer)
            # HvC: 0
            HvH: 1
            CvC: 2
        your choice: """)

    if game_type <= 1:
        players[-1] = "h"
        players[1] = "h"

    if game_type == 0:
        players[random.choice([-1, 1])] = "c"

    if game_type == 2:
        players[-1] = "c"
        players[1] = "c"


def turn(coordfrom=FALSE, coordto=FALSE):

    global dict_pieces, players, player, ia_type, difficulty
    if coordfrom != FALSE & coordto != FALSE:
        h_turn(coordfrom, coordto)
    while 1 & players[player] == 'c':
        # disable input
        c_turn(ia_type, difficulty)
        refresh_board()
    # enable input


# no longer used
def move_input():
    print("move (x1,y1) to (x2,y2):")
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    return (x1, y1), (x2, y2)


def h_turn(coordfrom, coordto):

    global player, dict_pieces

    move = (coordfrom, coordto)

    print("Turn: Player ", player)
    if dict_pieces[move[0]].player == player:
        if move[1] in dict_pieces[move[0]].list_move(move[0], dict_pieces):
            dict_pieces[move[1]] = dict_pieces.pop(move[0])
            if is_check(dict_pieces, player) == -player:
                print("Joueur ", -player, " en echec ! ")
            return True
        return False
    else:
        print("Pas votre pièce")
        return False


def c_turn(ia_type, difficulty):

    global player, dict_pieces
    print("Turn: Computer ", player)

    # calcule le coup a faire
    move = main_ia(player, dict_pieces, ia_type, difficulty)
    dict_pieces[move[1]] = dict_pieces.pop(move[0])
    dict_pieces[move[1]].has_moved = True
    return False
