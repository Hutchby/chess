# TODO: 7 classes de piece, une original et 6 qui en hérite, attribut coordonée et 2
# fonction de mouvement, une pour les possibilitées pour l'ia et l'autre pour
# verifier que le coup est possible

class Piece: #definition classe piece
    """ Classe définissant une piece caractérisée par :

            - sa position
            - son type (categorie)
            - son propriétaire
      """
    nbPieceP = [0, 0]

    def __init__(self): #constructeur
        self.position = [0, 0]
        self.player = 1

    def __init__(self, position, player): #constructeur
        self.position = position
        Piece.nbPieceP[player - 1] += 1
        self.player = player




class King(Piece): #definition classe roi qui hérite de Piece
    """ Classe définissant une piece caractérisée par :

            - sa position
            - son type (categorie)
            - son propriétaire
      """

    def __init__(self): #constructeur
        Piece.__init__(self)
        self.value = 1000
        self.symbol = "K"

    def __init__(self, position, player): #constructeur
        Piece.__init__(self, position, player)
        self.value = 1000
        self.symbol = "K"




class Queen(Piece): #definition classe roi qui hérite de Piece
    """ Classe définissant une piece caractérisée par :

            - sa position
            - son type (categorie)
            - son propriétaire
      """

    def __init__(self): #constructeur
        Piece.__init__(self)
        self.value = 8
        self.symbol = "Q"

    def __init__(self, position, player): #constructeur
        Piece.__init__(self, position, player)
        self.value = 8
        self.symbol = "Q"

class Bishop(Piece): #definition classe roi qui hérite de Piece
    """ Classe définissant une piece caractérisée par :

            - sa position
            - son type (categorie)
            - son propriétaire
      """

    def __init__(self): #constructeur
        self.value = 3
        Piece.__init__(self)
        self.symbol = "B"

    def __init__(self, position, player): #constructeur
        Piece.__init__(self, position, player)
        self.value = 3
        self.symbol = "B"

class Pawn(Piece): #definition classe roi qui hérite de Piece
    """ Classe définissant une piece caractérisée par :

            - sa position
            - son type (categorie)
            - son propriétaire
      """

    def __init__(self): #constructeur
        Piece.__init__(self)
        self.value = 1
        self.symbol = "P"

    def __init__(self, position, player): #constructeur
        Piece.__init__(self, position, player)
        self.value = 1
        self.symbol = "P"

class Rook(Piece): #definition classe roi qui hérite de Piece
    """ Classe définissant une piece caractérisée par :

            - sa position
            - son type (categorie)
            - son propriétaire
      """

    def __init__(self): #constructeur
        Piece.__init__(self)
        self.value = 5
        self.symbol = "R"

    def __init__(self, position, player): #constructeur
        Piece.__init__(self, position, player)
        self.value = 5
        self.symbol = "R"

class Knight(Piece): #definition classe roi qui hérite de Piece
    """ Classe définissant une piece caractérisée par :

            - sa position
            - son type (categorie)
            - son propriétaire
      """

    def __init__(self): #constructeur
        Piece.__init__(self)
        self.value = 3
        self.symbol = "Kn"

    def __init__(self, position, player): #constructeur
        Piece.__init__(self, position, player)
        self.value = 3
        self.symbol = "Kn"