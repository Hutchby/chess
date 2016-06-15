# rendu graphique pour le moment ta fonction de rendu

from tkinter import *

from src.rules import *


def afficherTerrain(listPiece):
    window = Tk()
    window.title("Plateau de jeu")
    canvas = Canvas(window, width=800, height=800)
    for n in range(1, 8):
        canvas.create_line(90 * n, 0, 90 * n, 720)
        canvas.create_line(0, 90 * n, 720, 90 * n)

    for n in range(8):
        canvas.create_text(n * 90 + 45, 755, text=itoa[n + 1])
        canvas.create_text(755, 720 - n * 90 - 45, text=8 - n)

    for position in listPiece:
        if listPiece[position].player == 1:
            color = "blue"
        else:
            color = "red"
        canvas.create_text(position[0] * 90 + 45, 720 - position[1] * 90 - 45, text=listPiece[position].symbol,
                           fill=color)
    canvas.pack()
    window.mainloop()
