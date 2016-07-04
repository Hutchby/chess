# TODO: comprendre le bug de la tour non définie
from src.pieces import *

itoa = {}
for i in range(8):
    itoa[i + 1] = chr(ord('A') + i)
print(itoa)

