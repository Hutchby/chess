# TODO: 7 classes de piece, une original et 6 qui en hérite, attribut coordonée et 2
# fonction de mouvement, une pour les possibilité pour l'ia et l'autre pour
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
        self.value = 0
        self.player = 1

    def __init__(self, position, value, player): #constructeur
        self.position = position
        Piece.nbPieceP[player - 1] += 1
        self.player = player



