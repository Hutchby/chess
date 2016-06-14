from src.pieces import *


def fonctionScore(listPiece, player):
    """ donne un score en fonction des pieces et de la distance au centre afin de pousser les pieces a se combattre
    Le controle du centre est important aux echecs sauf si il s’agit du roi.
    """

    score = 0

    for piece in listPiece:

        valuePiece = piece.value
        valuePiece *= 10

        # controler le centre est important
        if piece.symbol != "K":  # on controle pas le centre avec un roi
            valuePiece += 8 - abs(3.5 - piece.position[0]) - abs(3.5 - piece.position[1])

        if (piece.player != player):
            valuePiece *= -1

        score += valuePiece

    return score
