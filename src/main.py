#!/usr/bin/env python3
# gestion globale, variables globales et autres

from src.ai import *
from src.game import *

pieces = newSetOfPieces()
# """
print("list des mouvements", pieces[(2, 1)].symbol, " : ")
print(pieces[(2, 1)].list_move((2, 1), pieces))


for pos in pieces:
    print(pos, pieces[pos], ", ", pieces[pos].player)
# """

print(len(pieces))
# afficherTerrain(pieces)
# afficherTerrain(pieces, -1)

try:
    print("test: ", pieces[5, 5])
except Exception as excep:
    print("pieces[5,5] not exist")

print("score:", fonctionScore(pieces, 1))
game_type = -1

while game_type < 0 or 2 < game_type:
    game_type = input("""What kind of game? (H:human, C: computer)
        # HvC: 0
        HvH: 1
        CvC: 2
    your choice: """)
    game_type = int(game_type)
    print(game_type, type(game_type))
new_game(game_type, pieces)

type(pieces[5, 2])
pieces[5, 2].value
print(is_check(pieces, 1))
