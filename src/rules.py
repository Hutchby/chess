# Je suis pas sur que celui la soit necessaire

from src.pieces import *


def isCheck(listPiece, player):
    for piece in listPiece:
        x = piece.position[0]
        y = piece.position[1]
        if piece is King:
            if piece.player == player:
                for i in range(x, 8):
                    for piece2 in listPiece:
                        if piece2.position[0] == i & piece2.position[1] == y:
                            if piece2 is Queen or piece2 is Rook:
                                return True
                            else:
                                break

    return False


def newSetOfPieces():
    listPiece = []
    for i in [-1, 1]:
        for j in [-1, 1]:
            listPiece.append(Rook([int(3.5 + j * 3.5), int(3.5 + i * 3.5)], int((3 + i) / 2)))
            listPiece.append(Knight([int(3.5 + j * 2.5), int(3.5 + i * 3.5)], int((3 + i) / 2)))
            listPiece.append(Bishop([int(3.5 + j * 1.5), int(3.5 + i * 3.5)], int((3 + i) / 2)))

        for j in range(0, 8):
            listPiece.append(Pawn([j, int(3.5 + i * 2.5)], int((3 + i) / 2)))

        listPiece.append(Queen([int(3.5 + i * 0.5), int(3.5 + i * 3.5)], int((3 + i) / 2)))
        listPiece.append(King([int(3.5 - i * 0.5), int(3.5 + i * 3.5)], int((3 + i) / 2)))
    return listPiece
