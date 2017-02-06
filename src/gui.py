# rendu graphique pour le moment ta fonction de rendu

from tkinter import *

from src.rules import *
from src.game import *

window = Tk()
m = PanedWindow(window, orient=VERTICAL)
p = PanedWindow(m, orient=HORIZONTAL)
a = Entry(p, width=1)
b = Entry(p, width=1)
c = Entry(p, width=1)
d = Entry(p, width=1)

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


def send_coord():
    print("test")
    print(a.get(), b.get(), c.get(), d.get())
    return {a.get(), b.get(), c.get(), d.get()}


def main_windows():
    pieces = newSetOfPieces()
    window.title("Chess by Popino et Lulu")

    global window, m, p, a, b, c, d

    m.pack(pady=2, padx=2)
    p.add(Label(p, text='from', background='white', anchor=CENTER))
    p.add(a)
    p.add(b)
    p.add(Label(p, text='to', background='white', anchor=CENTER))
    p.add(c)
    p.add(d)
    p.add(Label(p, text='', background='grey', anchor=CENTER))

    z = PanedWindow(m, orient=HORIZONTAL)
    z.add(Button(z, text='play', command=send_coord))
    z.add(Button(z, text='quit', command=window.quit))
    z.add(Label(z, text='', background='grey', anchor=CENTER))

    m.add(cenvas_field(window, pieces))
    m.add(p)
    m.add(z)
    m.pack()
    window.mainloop()
