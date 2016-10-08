from src.pieces import *
import random


def fonction_score(pieces, player):
    """ donne un score en fonction des pieces et de la distance au centre afin de pousser les pieces a se combattre
    Le controle du centre est important aux echecs sauf si il s’agit du roi.
    """

    score = 0

    for pos in pieces:

        valuePiece = pieces[pos].value
        valuePiece *= 10

        # controler le centre est important
        if pieces[pos].symbol != "K":  # on controle pas le centre avec un roi
            valuePiece += 8 - abs(3.5 - pos[0]) - abs(3.5 - pos[1])

        if pieces[pos].player != player:
            valuePiece *= -1

        score += valuePiece

        # on regarde si on met en echec
    if is_check(pieces, player):
        score += 20

    return score


def random_move(pieces, player):
    player_p = player
    while player_p == player:
        current_piece = random.choice(list(pieces.keys()))
        player_p = pieces[current_piece].player
        if pieces[current_piece].list_move(current_piece, pieces) == []:
            player_p = player

    move_ok = player
    # while move_ok == player:
    move = (current_piece, random.choice(pieces[current_piece].list_move(current_piece, pieces)))
    print(pieces[current_piece], " ", move)
    return move


def viral_spread(pieces, player, diff):
    list_move = list_all_move(pieces, player)
    list_score = [0] * len(list_move)
    list_nb_move = [0] * len(list_move)
    move = list_move[max_indice(list_score)]
    return move


def mainIA(player, pieces):
    # ia basique, random move
    move = random_move(pieces, player)
    return move
