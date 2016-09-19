#TODO: valider que les coups dans la liste de coups autorisés

from src.gui import *
from src.pieces import *
from src.ai import *


def move_input():
    print("move (x1,y1) to (x2,y2):")
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    return (x1, y1), (x2, y2)


def h_turn(player, dico_piece):

    check = 1
    while check != 0:
        temp = 0
        print("Turn: Player ", player)
        afficherTerrain(dico_piece, player)
        move = move_input()

        if there_is_something(dico_piece, move[1][0], move[1][1]):
            temp = dico_piece.pop(move[1])

        # on vérifie que le joueur bouge bien sa piece
        if dico_piece[move[0]].player == player:
            if (1): #dico_piece[move[0]].list_move(move[0], dico_piece) == move[1]:
                dico_piece[move[1]] = dico_piece.pop(move[0])

            # verifier que le coup est possible

            # verifier si échec
                check = is_check(dico_piece, player)
                if check == player:
                    print("Impossible de jouer ce coup")
                    dico_piece[move[0]] = dico_piece.pop(move[1])
                    dico_piece[move[1]].has_moved = True
                    if temp:
                        dico_piece[move[1]] = temp

                if check == -player:
                    print("Joueur ", -player, " en echec ! ")
                    break
                else:
                    print("Coup impossible !")
        else:
            print("Pas votre pièce")

    return False


def c_turn(player, dico_piece):
    print("Turn: Computer ", player)

    # calcule le coup a faire
    move = mainIA(player, dico_piece)
    dico_piece[move[1]] = dico_piece.pop(move[0])
    dico_piece[move[1]].has_moved = True


    return False


def hh_game(dico_piece):
    finish = True
    player = -1
    while finish:
        h_turn(player, dico_piece)
        player = -player  # swap player turn
        finish = TRUE


def cc_game(dico_piece):
    finish = True
    player = 1
    while finish:
        c_turn(player, dico_piece)
        player = -player  # swap player turn
        #finish = False
        afficherTerrain(dico_piece, player)
    return False


def hc_game(dico_piece):
    finish = True
    h_is = 1
    player = 1
    while finish:
        if h_is == player:
            finish = h_turn(player, dico_piece)
        else:
            finish = c_turn(player, dico_piece)
        player = -player  # swap player turn
    return False


def new_game(game_type, dico_piece):
    if game_type == 0:
        print("Human vs Computer: The game can start")
        hc_game(dico_piece)
    elif game_type == 2:
        print("Computer vs Computer: The game can start")
        cc_game(dico_piece)
    elif game_type == 1:
        print("Human vs Human: The game can start")
        hh_game(dico_piece)
