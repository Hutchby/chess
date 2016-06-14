#! user/bin/env python3


# gestion globale, variables globales et autres

from src.gui import *
from src.rules import *
from src.game import *
from src.ai import *

print("Hello World")

listPiece = newSetOfPieces()

afficherTerrain(listPiece)

print(len(listPiece))

print(listPiece[1].symbol)
print(listPiece[1].player)

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

