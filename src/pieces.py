# TODO: 7 classes de piece, une original et 6 qui en hérite, attribut coordonée et 2
# fonction de mouvement, une pour les possibilitées pour l'ia et l'autre pour
# verifier que le coup est possible


class Piece:  # definition classe piece
    """ Classe définissant une piece caractérisée par :
            - sa position
            - son type (categorie)
            - son propriétaire
      """

    def __init__(self, position=(0, 0), player=1):  # constructeur
        has_moved = False
        self.position = position  # un tuple c'est carrément plus propre et ca evite les conneries
        self.player = player
        self.value = 0
        self.symbol = "none"

    def try_move(self, pos_a, pos_b) -> bool:  # pour verifier les coups joués
        print("Faute de jeu! Tu bois!")
        return False

    def list_move(self):  # list les coup possible pour une piece donnée
        print("Je retourne pas les possibilité pour le moment alors bon...")
        return 0, 0


class King(Piece):  # definition classe ROI qui hérite de Piece

    def __init__(self, position, player):  # constructeur
        super().__init__(position, player)
        self.value = 1000
        self.symbol = "Ki"


class Queen(Piece):  # definition classe REINE qui hérite de Piece

    def __init__(self, position, player):  # constructeur
        super().__init__(position, player)
        self.value = 8
        self.symbol = "Qu"


class Bishop(Piece):  # definition classe FOU qui hérite de Piece

    def __init__(self, position, player):  # constructeur
        super().__init__(position, player)
        self.value = 3
        self.symbol = "Bs"


class Pawn(Piece):  # definition classe PION qui hérite de Piece

    def __init__(self, position, player):  # constructeur
        super().__init__(position, player)
        self.value = 1
        self.symbol = "Pn"


class Rook(Piece):  # definition classe TOUR qui hérite de Piece

    def __init__(self, position, player):  # constructeur
        super().__init__(position, player)
        self.value = 5
        self.symbol = "Rk"


class Knight(Piece):  # definition classe Cavalier qui hérite de Piece

    def __init__(self, position, player):  # constructeur
        super().__init__(position, player)
        self.value = 3
        self.symbol = "Kn"
