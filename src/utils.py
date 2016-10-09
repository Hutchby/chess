from copy import deepcopy
from src.rules import *
from src.gui import *
from src.pieces import *
from src.ai import *

def max_indice(list):
    maxi = 0
    for i in range(0, len(list)):
        if list[i] > list[maxi]:
            maxi = i
    return maxi

def min_indice(list):
    mini = 0
    for i in list:
        if list[i] < list[mini]:
            mini = i
    return mini
