#! user/bin/env python3
# gestion globale, variables globales et autres

from src.ai import *
from src.game import *
from src.gui import *
from src.rules import *

print("Hello World")

listPiece = newSetOfPieces()

for pos in listPiece:
    print(pos, listPiece[pos].symbol, ", ", listPiece[pos].player)

afficherTerrain(listPiece)

print(len(listPiece))

try:
    print("test: ", listPiece[5,5])
except Exception as excep:
    print("listPiece[5,5] not exist")

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
