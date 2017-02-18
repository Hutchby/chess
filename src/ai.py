# TODO: check function score

from src.pieces import *
from src.utils import *
import random


# to be improved
def function_score(pieces, player):
    """ donne un score en fonction des pieces et de la distance au centre afin de pousser les pieces a se combattre
    Le controle du centre est important aux echecs sauf si il s’agit du roi.
    """

    score = 0

    for pos in pieces:

        value_piece = pieces[pos].value
        value_piece *= 10

        # controler le centre est important
        if pieces[pos].symbol != "K":  # on controle pas le centre avec un roi
            value_piece += 8 - abs(4.5 - pos[0]) - (pos[1] - 4.5) * pieces[pos].player

        if pieces[pos].player != player:
            value_piece *= -1

        score += value_piece

        # on regarde si on met en echec
    if is_check(pieces, player):
        score += 20

    return score


def random_move(pieces, player):
    return random.choice(list_all_move(pieces, player))


def viral_spread(pieces, player, nb_try, diff=3):
    list_move = random.sample(list_all_move(pieces, player), nb_try)
    list_score = [0] * nb_try
    for i in range(0, nb_try):
        first_move = list_move[i]
        pieces_temp = deepcopy(pieces)
        pieces_temp[first_move[1]] = pieces_temp.pop(first_move[0])
        current_player = player
        for t in range(0, diff):
            current_player *= -1
            move = random_move(pieces_temp, current_player)
            pieces_temp[move[1]] = pieces_temp.pop(move[0])
        list_score[i] = function_score(pieces_temp, player)

    # list_nb_move = [0] * len(list_move)
    move = list_move[max_index(list_score)]
    print(list_score)
    return move


def max_score(pieces, player):
    list_move = list_all_move(pieces, player)
    list_score = [0] * len(list_move)
    for i in range(0, len(list_move)):
        first_move = list_move[i]
        pieces_temp = deepcopy(pieces)
        pieces_temp[first_move[1]] = pieces_temp.pop(first_move[0])
        list_score[i] = function_score(pieces_temp, player)
    index = max_index(list_score)
    return [list_move[index], list_score[index]]


def best_move(pieces, player, deep):
    # generate list of all move & generate an empty list of score
    list_move = list_all_move(pieces, player)
    list_score = [0] * len(list_move)

    # stop condition of the reccursiv loop
    if deep == 1:
        for i in range(0, len(list_move)):
            # generate a copy of the dictionnary to try a move
            pieces_temp = deepcopy(pieces)

            # make the move & calculate the score
            first_move = list_move[i]
            pieces_temp[first_move[1]] = pieces_temp.pop(first_move[0])
            list_score[i] = function_score(pieces_temp, player)

        # find the best score and return it
        index = max_index(list_score)
        return [list_move[index], list_score[index]]

    for t in range(0, len(list_move)):
        move = list_move[t]
        pieces_temp = deepcopy(pieces)
        pieces_temp[move[1]] = pieces_temp.pop(move[0])
        [list_move[t], list_score[t]] = best_move(pieces_temp, -player, deep - 1)
    if deep % 2 == 1:
        index = max_index(list_score)
    else:
        index = min_index(list_score)
    return [list_move[index], list_score[index]]


def main_ia(player, pieces, ia_type, difficulty):
    # basic ia, random move
    if ia_type == "random":
        move = random_move(pieces, player)

    elif ia_type == "viral":
        nb_try = 10
        move = viral_spread(pieces, player, nb_try, difficulty)
    # best next move according to score function
    elif ia_type == "max_score":
        move = max_score(pieces, player)[0]

    # best move to a specific deep according to score function
    elif ia_type == "best_move":
        move = best_move(pieces, player, 2)[0]
    else:
        print("error not the right IA selected")
        move = ""
    dict_pieces[move[1]] = dict_pieces.pop(move[0])
