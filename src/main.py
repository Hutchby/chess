#! user/bin/env python3


# gestion globale, variables globales et autres

from operator import itemgetter

from src.ai import *
from src.game import *
from src.gui import *
from src.rules import *

print("Hello World")

listPiece = newSetOfPieces()
print(listPiece)

for pos in listPiece:
    print(pos, type(listPiece[pos]), listPiece[pos].player)

afficherTerrain(listPiece)

print(len(listPiece))

for i in range(8, 0):
    print(i)

print(fonctionScore(listPiece, 1))
game_type = -1

while game_type < 0 or 2 < game_type:
    game_type = input("""What kind of game? (H:human, C: computer)
        HvC: 0
        HvH: 1
        CvC: 2
    your choice: """)
    game_type = int(game_type)
    print(game_type, type(game_type))
new_game(game_type)
