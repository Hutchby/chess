# TODO: 7 classes de piece, une original et 6 qui en hérite, attribut coordonée et 2
# fonctions de mouvement, une pour les possibilitées pour l'ia et l'autre pour
# verifier que le coup est possible

from src.rules import isCheck


def there_is_something(d, x, y):
    try:
        res = d[x, y]
    except Exception:
        return False
    return d[x, y]


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
                if 2*i + j != 0:
                    dico_piece_temp = dico_piece
                    dico_piece_temp[(pos[0]+i, pos[1]+j)] = dico_piece_temp.pop(pos)
                    if not isCheck(dico_piece_temp, self.player) == self.player:
                        l.append((pos[0]+i, pos[1]+j))
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
