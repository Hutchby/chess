# TODO: comprendre le bug de la tour non définie
from src.pieces import *

itoa = {}
for i in range(8):
    itoa[i + 1] = chr(ord('A') + i)
print(itoa)


def isCheck(dict_piece, player):
    # on récupère les rois
    state = 0
    for roi in dict_piece:
        if type(dict_piece[roi]) == King:
            # echecs dans les 4 directions principales
            for x in range(roi[0]+1, 9):
                if there_is_something(dict_piece, x, roi[1]):
                    if type(dict_piece[x, roi[1]]) == Queen or type(dict_piece[x, roi[1]]) == Rook:
                        if dict_piece[x, roi[1]].player != dict_piece[roi].player:
                            if dict_piece[roi].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
                    break

            for x in range(roi[0]-1, 0, -1):
                if there_is_something(dict_piece, x, roi[1]):
                    if type(dict_piece[x, roi[1]]) == Queen or type(dict_piece[x, roi[1]]) == Rook:
                        if dict_piece[x, roi[1]].player != dict_piece[roi].player:
                            if dict_piece[roi].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
                    break

            for y in range(roi[1]+1, 9):
                if there_is_something(dict_piece, roi[0], y):
                    if type(dict_piece[roi[0], y]) == Queen or type(dict_piece[roi[0], y]) == Rook:
                        if dict_piece[roi[0], y].player != dict_piece[roi].player:
                            if dict_piece[roi].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
                    break

            for y in range(roi[1]-1, 0, -1):
                if there_is_something(dict_piece, roi[0], y):
                    if type(dict_piece[roi[0], y]) == Queen or type(dict_piece[roi[0], y]) == Rook:
                        if dict_piece[roi[0], y].player != dict_piece[roi].player:
                            if dict_piece[roi].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
                    break

            # echec suivant les diagonales

            # en haut à droite
            for x in range(roi[0]+1, 9):
                if roi[0] + x > 8 or roi[1] + x > 8:
                    break
                piece = (roi[0] + x, roi[1] + x)
                if there_is_something(dict_piece, piece[1], piece[2]):
                    if type(dict_piece[piece]) == Queen or type(dict_piece[piece]) == Bishop:
                        if dict_piece[piece].player != dict_piece[roi].player:
                            if dict_piece[piece].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
            # en haut à gauche
            for x in range(roi[0]+1, 9):
                if roi[0] - x < 1 or roi[1] + x > 8:
                    break
                piece = (roi[0] - x, roi[1] + x)
                if there_is_something(dict_piece, piece[1], piece[2]):
                    if type(dict_piece[piece]) == Queen or type(dict_piece[piece]) == Bishop:
                        if dict_piece[piece].player != dict_piece[roi].player:
                            if dict_piece[piece].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
            # en bas à droite
            for x in range(roi[0]+1, 9):
                if roi[0] + x > 8 or roi[1] - x < 1:
                    break
                piece = (roi[0] + x, roi[1] - x)
                if there_is_something(dict_piece, piece[1], piece[2]):
                    if type(dict_piece[piece]) == Queen or type(dict_piece[piece]) == Bishop:
                        if dict_piece[piece].player != dict_piece[roi].player:
                            if dict_piece[piece].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
            # en bas à gauche
            for x in range(roi[0]+1, 9):
                if roi[0] - x < 1 or roi[1] - x < 1:
                    break
                piece = (roi[0] - x, roi[1] - x)
                if there_is_something(dict_piece, piece[0], piece[1]):
                    if type(dict_piece[piece]) == Queen or type(dict_piece[piece]) == Bishop:
                        if dict_piece[piece].player != dict_piece[roi].player:
                            if dict_piece[piece].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player
            # echecs roi
            dist = [-1, 0, 1]
            for x in dist:
                for y in dist:
                    if abs(x) + abs(y) > 0:
                        piece = (roi[0] + x, roi[1] + y)
                        if there_is_something(dict_piece, piece[0], piece[1]):
                            if type(dict_piece[piece]) == King:
                                    if dict_piece[piece].player != dict_piece[roi].player:
                                        if dict_piece[piece].player == player:
                                            return dict_piece[roi].player
                                        state = dict_piece[roi].player

            # echecs pions
            for x in [-1, 1]:
                piece = (roi[0] + x, roi[1] - dict_piece[roi].player)
                if there_is_something(dict_piece, piece[0], piece[1]):
                    if type(dict_piece[piece]) == Pawn:
                        if dict_piece[piece].player != dict_piece[roi].player:
                            if dict_piece[piece].player == player:
                                return dict_piece[roi].player
                            state = dict_piece[roi].player

            # echecs cavaliers
            dist = [-2, -1, 1, 2]
            for x_dist in dist:
                for y_dist in dist:
                    if abs(x_dist) + abs(y_dist) == 3:
                        piece = (roi[0] + x_dist, roi[1] + y_dist)
                        if there_is_something(dict_piece, piece[0], piece[1]):
                            if type(dict_piece[piece]) == Knight:
                                if dict_piece[piece].player != dict_piece[roi].player:
                                    if dict_piece[piece].player == player:
                                        return dict_piece[roi].player
                                    state = dict_piece[roi].player
    return state


def newSetOfPieces():
    dict_piece = {}
    for i in [-1, 1]:
        for j in [-1, 1]:
            dict_piece[int(4.5 + j * 3.5), int(4.5 + i * 3.5)] = Piece(i)
            dict_piece[int(4.5 + j * 2.5), int(4.5 + i * 3.5)] = Knight(i)
            dict_piece[int(4.5 + j * 1.5), int(4.5 + i * 3.5)] = Bishop(i)

        for j in range(1, 9):
            dict_piece[j, int(4.5 + i * 2.5)] = Pawn(i)

        dict_piece[int(4.5 + i * 0.5), int(4.5 + i * 3.5)] = Queen(i)
        dict_piece[int(4.5 - i * 0.5), int(4.5 + i * 3.5)] = King(i)
    return dict_piece
