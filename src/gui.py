# rendu graphique pour le moment ta fonction de rendu

from tkinter import *

from src.rules import *
from src.game import *


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


def cenvas_field(window, pieces, player=-1):
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
    return canvas


def test():
    print("lol")


def test2():
    print("troll")


def main_windows():
    pieces = newSetOfPieces()
    window = Tk()
    window.title("Chess by Popino et Lulu")

    m = PanedWindow(window, orient=VERTICAL, )
    m.pack(pady=2, padx=2)

    p = PanedWindow(m, orient=HORIZONTAL)
    p.add(Label(p, text='from', background='white', anchor=CENTER))
    p.add(Entry(p, textvariable=str, width=1))
    p.add(Entry(p, textvariable=str, width=1))
    p.add(Label(p, text='to', background='white', anchor=CENTER))
    p.add(Entry(p, textvariable=str, width=1))
    p.add(Entry(p, textvariable=str, width=1))
    p.add(Label(p, text='', background='grey', anchor=CENTER))

    d = PanedWindow(m, orient=HORIZONTAL)
    d.add(Button(d, text='play', command=turn))
    d.add(Button(d, text='quit', command=window.quit))
    d.add(Label(d, text='', background='grey', anchor=CENTER))

    m.add(cenvas_field(window, pieces))
    m.add(p)
    m.add(d)
    m.pack()
    window.mainloop()
