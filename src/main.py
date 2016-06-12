#! user/bin/env python3


# gestion globale, variables globales et autres

from src.pieces import *
from src.gui import *
from src.rules import *
from src.ai import *

print("Hello World")

listPiece = newGame()

afficherTerrain(listPiece)

print(len(listPiece))

print(listPiece[1].symbol)
print(listPiece[1].player)


for i in range(8,0):
    print(i)

print(fonctionScore(listPiece, 1))