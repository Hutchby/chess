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
            valuePiece += 8 - abs(4.5 - pos[0]) - (pos[1] - 4.5) * pieces[pos].player

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
    return move


def viral_spread(pieces, player, diff, nb_try):
    diff = 3 # à enlever à terme
    list_move = list_all_move(pieces, player)
    list_score = [0] * len(list_move)
    for i in range(0, len(list_move)):
        first_move = list_move[i]
        try_move(pieces, player, first_move)
        pieces_temp = deepcopy(pieces)
        pieces_temp[first_move[1]] = pieces_temp.pop(first_move[0])
        for t in range(0, nb_try):
            current_player = player
            for s in range(0, diff):
                current_player *= -1
                move = random_move(pieces_temp, current_player)
                pieces_temp[move[1]] = pieces_temp.pop(move[0])
            list_score[i] += fonction_score(pieces_temp, player)
        # list_score[i] = fonction_score(pieces_temp, player)

    list_nb_move = [0] * len(list_move)
    move = list_move[max_indice(list_score)]
    print(list_score)
    return move


def maxScore(pieces, player):
    list_move = list_all_move(pieces, player)
    list_score = [0] * len(list_move)
    for i in range(0, len(list_move)):
        first_move = list_move[i]
        # try_move(pieces, player, first_move) # pas utile car mouvement dékà testé dans list_all_move
        pieces_temp = deepcopy(pieces)
        pieces_temp[first_move[1]] = pieces_temp.pop(first_move[0])
        list_score[i] = fonction_score(pieces_temp, player)
        indice = max_indice(list_score)
    return [list_move[indice], list_score[indice]]


def best_move(pieces, player, deep):
    list_move = list_all_move(pieces, player)
    list_score = [0] * len(list_move)
    if deep == 1:
        for i in range(0, len(list_move)):
            first_move = list_move[i]
            # try_move(pieces, player, first_move) # pas utile car mouvement dékà testé dans list_all_move
            pieces_temp = deepcopy(pieces)
            pieces_temp[first_move[1]] = pieces_temp.pop(first_move[0])
            list_score[i] = fonction_score(pieces_temp, player)
            indice = max_indice(list_score)
        return [list_move[indice], list_score[indice]]

    for i in range(0, len(list_move)):
        move = list_move[i]
        pieces_temp = deepcopy(pieces)
        pieces_temp[move[1]] = pieces_temp.pop(move[0])
        [list_move[i], list_score[i]] = best_move(pieces_temp, -player, deep - 1)
    if deep % 2 == 1:
        indice = max_indice(list_score)
    else:
        indice = min_indice(list_score)
    return [list_move[indice], list_score[indice]]


def mainIA(player, pieces, ia_type, difficulty):
    # ia basique, random move
    if ia_type == "random":
        move = random_move(pieces, player, 0)
    elif ia_type == "viral":
        nb_try = 10
        move = viral_spread(pieces, player, difficulty, nb_try)
    elif ia_type == "maxScore":
        move = maxScore(pieces, player)[0]
    elif ia_type == "best_move":
        move = best_move(pieces, player, 2)[0]
    return move


