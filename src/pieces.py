# TODO: 7 classes de piece, une original et 6 qui en hérite, attribut coordonée et 2
# fonctions de mouvement, une pour les possibilitées pour l'ia et l'autre pour
# verifier que le coup est possible

from src.rules import *


def there_is_something(d, x, y):
    try:
        res = d[x, y]
    except Exception:
        return False
    return res


"""
    Classe définissant une piece caractérisée par :
        - sa position
        - son type (categorie)
        - son propriétaire
"""


class Piece:  # definition classe piece

    def __init__(self, player=1):  # constructeur
        self.has_moved = False
        self.player = player
        self.value = 0
        self.symbol = "none"

    def __repr__(self):
        return Piece

    def try_move(self, pos_a, pos_b) -> bool:  # pour verifier les coups joués
        print("Faute de jeu! Tu bois!")
        return False

    def list_move(self, pos, dico_piece):  # list les coup possible pour une piece donnée
        l = []  # liste de tuple x/y
        print("Je retourne pas les possibilité pour le moment alors bon...")
        return l


class King(Piece):  # definition classe ROI qui hérite de Piece

    def __init__(self, player):  # constructeur
        super().__init__(player)
        self.value = 1000
        self.symbol = "Ki"

    def __repr__(self):
        return "King"

    def list_move(self, pos, dico_piece):  # list les coup possible pour une piece donnée
        l = []  # liste de tuple x/y

        for i in range(-1, 1):
            for j in range(-1, 1):
                if 2 * i + j != 0:
                    dico_piece_temp = dico_piece
                    dico_piece_temp[(pos[0] + i, pos[1] + j)] = dico_piece_temp.pop(pos)
                    if not isCheck(dico_piece_temp, self.player) == self.player:
                        l.append((pos[0] + i, pos[1] + j))
        return l


class Queen(Piece):  # definition classe REINE qui hérite de Piece

    def __init__(self, player):  # constructeur
        super().__init__(player)
        self.value = 8
        self.symbol = "Qu"

    def __repr__(self):
        return "Queen"


class Bishop(Piece):  # definition classe FOU qui hérite de Piece

    def __init__(self, player):  # constructeur
        super().__init__(player)
        self.value = 3
        self.symbol = "Bs"

    def __repr__(self):
        return "Bishop"


class Pawn(Piece):  # definition classe PION qui hérite de Piece

    def __init__(self, player):  # constructeur
        super().__init__(player)
        self.value = 1
        self.symbol = "Pn"

    def __repr__(self):
        return "Pawn"

    def list_move(self, pos, dico_piece):  # list les coup possible pour une piece donnée
        l = []

        # prendre en diagonale
        for i in [-1, 1]:
            position = (pos[0] + i, pos[1] - self.player)
            if there_is_something(dico_piece, position[0], position[1]):
                if dico_piece[position].player != self.player:
                    l.append(position)

        # avancer d'une case
        position = (pos[0], pos[1] - self.player)
        if there_is_something(dico_piece, position[0], position[1]):
            return l
        l.append(position)

        # avancer de 2 cases
        if not self.has_moved:
            position = (position[0], position[1] - self.player)
            if not there_is_something(dico_piece, position[0], position[1]):
                l.append(position)
        return l


class Rook(Piece):  # definition classe TOUR qui hérite de Piece

    def __init__(self, player):  # constructeur
        super().__init__(player)
        self.value = 5
        self.symbol = "Rk"

    def __repr__(self):
        return "Rook"


class Knight(Piece):  # definition classe Cavalier qui hérite de Piece

    def __init__(self, player):  # constructeur
        super().__init__(player)
        self.value = 3
        self.symbol = "Kn"

    def __repr__(self):
        return "Knight"


def newSetOfPieces():
    dict_piece = {}
    for i in [-1, 1]:
        for j in [-1, 1]:
            print("test")
            dict_piece[int(4.5 + j * 3.5), int(4.5 + i * 3.5)] = Rook(i)
            dict_piece[int(4.5 + j * 2.5), int(4.5 + i * 3.5)] = Knight(i)
            dict_piece[int(4.5 + j * 1.5), int(4.5 + i * 3.5)] = Bishop(i)

        for j in range(1, 9):
            dict_piece[j, int(4.5 + i * 2.5)] = Pawn(i)

        dict_piece[int(4.5 + i * 0.5), int(4.5 + i * 3.5)] = Queen(i)
        dict_piece[int(4.5 - i * 0.5), int(4.5 + i * 3.5)] = King(i)
    return dict_piece


def isCheck(dict_piece, player):
    # on récupère les rois
    state = 0
    for roi in dict_piece:
        if type(dict_piece[roi]) == King:
            # echecs dans les 4 directions principales
            for x in range(roi[0] + 1, 9):
                if there_is_something(dict_piece, x, roi[1]):
                    if type(dict_piece[x, roi[1]]) == Queen or type(dict_piece[x, roi[1]]) == Rook:
                        if dict_piece[x, roi[1]].player != dict_piece[roi].player:
                            if dict_piece[roi].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
                    break

            for x in range(roi[0] - 1, 0, -1):
                if there_is_something(dict_piece, x, roi[1]):
                    if type(dict_piece[x, roi[1]]) == Queen or type(dict_piece[x, roi[1]]) == Rook:
                        if dict_piece[x, roi[1]].player != dict_piece[roi].player:
                            if dict_piece[roi].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
                    break

            for y in range(roi[1] + 1, 9):
                if there_is_something(dict_piece, roi[0], y):
                    if type(dict_piece[roi[0], y]) == Queen or type(dict_piece[roi[0], y]) == Rook:
                        if dict_piece[roi[0], y].player != dict_piece[roi].player:
                            if dict_piece[roi].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
                    break

            for y in range(roi[1] - 1, 0, -1):
                if there_is_something(dict_piece, roi[0], y):
                    if type(dict_piece[roi[0], y]) == Queen or type(dict_piece[roi[0], y]) == Rook:
                        if dict_piece[roi[0], y].player != dict_piece[roi].player:
                            if dict_piece[roi].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
                    break

            # echec suivant les diagonales

            # en haut à droite
            for x in range(roi[0] + 1, 9):
                if roi[0] + x > 8 or roi[1] + x > 8:
                    break
                piece = (roi[0] + x, roi[1] + x)
                if there_is_something(dict_piece, piece[1], piece[2]):
                    if type(dict_piece[piece]) == Queen or type(dict_piece[piece]) == Bishop:
                        if dict_piece[piece].player != dict_piece[roi].player:
                            if dict_piece[piece].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
            # en haut à gauche
            for x in range(roi[0] + 1, 9):
                if roi[0] - x < 1 or roi[1] + x > 8:
                    break
                piece = (roi[0] - x, roi[1] + x)
                if there_is_something(dict_piece, piece[1], piece[2]):
                    if type(dict_piece[piece]) == Queen or type(dict_piece[piece]) == Bishop:
                        if dict_piece[piece].player != dict_piece[roi].player:
                            if dict_piece[piece].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
            # en bas à droite
            for x in range(roi[0] + 1, 9):
                if roi[0] + x > 8 or roi[1] - x < 1:
                    break
                piece = (roi[0] + x, roi[1] - x)
                if there_is_something(dict_piece, piece[1], piece[2]):
                    if type(dict_piece[piece]) == Queen or type(dict_piece[piece]) == Bishop:
                        if dict_piece[piece].player != dict_piece[roi].player:
                            if dict_piece[piece].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
            # en bas à gauche
            for x in range(roi[0] + 1, 9):
                if roi[0] - x < 1 or roi[1] - x < 1:
                    break
                piece = (roi[0] - x, roi[1] - x)
                if there_is_something(dict_piece, piece[0], piece[1]):
                    if type(dict_piece[piece]) == Queen or type(dict_piece[piece]) == Bishop:
                        if dict_piece[piece].player != dict_piece[roi].player:
                            if dict_piece[piece].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
            # echecs roi
            dist = [-1, 0, 1]
            for x in dist:
                for y in dist:
                    if abs(x) + abs(y) > 0:
                        piece = (roi[0] + x, roi[1] + y)
                        if there_is_something(dict_piece, piece[0], piece[1]):
                            if type(dict_piece[piece]) == King:
                                if dict_piece[piece].player != dict_piece[roi].player:
                                    if dict_piece[piece].player == player:
                                        return dict_piece[roi].player
                                    state = dict_piece[roi].player

            # echecs pions
            for x in [-1, 1]:
                piece = (roi[0] + x, roi[1] - dict_piece[roi].player)
                if there_is_something(dict_piece, piece[0], piece[1]):
                    if type(dict_piece[piece]) == Pawn:
                        if dict_piece[piece].player != dict_piece[roi].player:
                            if dict_piece[piece].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player

            # echecs cavaliers
            dist = [-2, -1, 1, 2]
            for x_dist in dist:
                for y_dist in dist:
                    if abs(x_dist) + abs(y_dist) == 3:
                        piece = (roi[0] + x_dist, roi[1] + y_dist)
                        if there_is_something(dict_piece, piece[0], piece[1]):
                            if type(dict_piece[piece]) == Knight:
                                if dict_piece[piece].player != dict_piece[roi].player:
                                    if dict_piece[piece].player == player:
                                        return dict_piece[roi].player
                                    state = dict_piece[roi].player
    return state
