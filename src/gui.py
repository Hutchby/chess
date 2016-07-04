# rendu graphique pour le moment ta fonction de rendu

from tkinter import *

from src.rules import *


def afficherTerrain(pieces, player=-1):
    window = Tk()
    window.title("Plateau de jeu")
    canvas = Canvas(window, width=800, height=800)
    for n in range(1, 8):
        canvas.create_line(90 * n, 0, 90 * n, 720)
        canvas.create_line(0, 90 * n, 720, 90 * n)

    for n in range(8):

        if player == 1:
            canvas.create_text(755, 675 - n * 90, text=8 - n)
            canvas.create_text(n * 90 + 45, 755, text=itoa[8 - n])
        else:
            canvas.create_text(755, 675 - n * 90, text=n + 1)
            canvas.create_text(n * 90 + 45, 755, text=itoa[n + 1])

    for pos in pieces:
        if pieces[pos].player == -1:
            color = "blue"
        else:
            color = "red"
        if player == -1:
            canvas.create_text(pos[0] * 90 - 45, 765 - pos[1] * 90, text=pieces[pos].symbol, fill=color)
        else:
            canvas.create_text(765 - pos[0] * 90, pos[1] * 90 - 45, text=pieces[pos].symbol, fill=color)
    canvas.pack()
    window.mainloop()
