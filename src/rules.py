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
            print(dict_piece[roi])
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
    return state


def newSetOfPieces():
    dict_piece = {}
    for i in [-1, 1]:
        for j in [-1, 1]:
            dict_piece[int(4.5 + j * 3.5), int(4.5 + i * 3.5)] = Rook(i)
            dict_piece[int(4.5 + j * 2.5), int(4.5 + i * 3.5)] = Knight(i)
            dict_piece[int(4.5 + j * 1.5), int(4.5 + i * 3.5)] = Bishop(i)

        for j in range(1, 9):
            dict_piece[j, int(4.5 + i * 2.5)] = Pawn(i)

        dict_piece[int(4.5 + i * 0.5), int(4.5 + i * 3.5)] = Queen(i)
        dict_piece[int(4.5 - i * 0.5), int(4.5 + i * 3.5)] = King(i)
    return dict_piece
