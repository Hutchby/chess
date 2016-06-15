from src.pieces import *


def fonctionScore(pieces, player):
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

    return score
