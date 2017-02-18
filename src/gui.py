# rendu graphique pour le moment ta fonction de rendu

from tkinter import *

from src.rules import *
from src.game import *

window = Tk()
m = PanedWindow(window, orient=VERTICAL)
p = PanedWindow(m, orient=HORIZONTAL)
fclick = []

def set_buttons(main_w):
    ret = []
    for i in range(0, 8):
        ret.append([])
        for j in range(0, 8):
            ret[i].append(Button(main_w, text='_', command=lambda i=i, j=j: OnButtonClick(i, j)))
            ret[i][j].grid(row=j, column=i + 1)
    return ret


board = set_buttons(window)


def refresh_board():
    global dict_pieces, board

    print(dict_pieces.keys())
    for i in range(0, 8):
        for j in range(0, 8):
            board[i][j].config(text='   ')
    for pos in dict_pieces.keys():
        board[pos[0] - 1][pos[1] - 1].config(text=dict_pieces[pos].symbol)


def OnButtonClick(i, j):
    global fclick, player
    print(i, j)
    if len(fclick) == 0:
        fclick = [i, j]
    else:
        return
#        turn(dict_pieces, player, [fclick, [i, j]])


def send_coord():
    global dict_pieces, player
    print("test")
    # dict_pieces[3, 3] = Bishop(1)
    move = []
    for i in range(0,4):
        move.append(user_input[i].get())
    print(move)

    # turn()
    refresh_board()
    return move


def set_input(main_w):
    ret = [Entry(main_w, width=2), Entry(main_w, width=2), Entry(main_w, width=2), Entry(main_w, width=2)]
    ret[0].grid(row=9, column=3)
    ret[1].grid(row=9, column=4)
    ret[2].grid(row=9, column=6)
    ret[3].grid(row=9, column=7)
    Label(main_w, text='from', background='white', anchor=CENTER).grid(row=9, column=2)
    Label(main_w, text='to', background='white', anchor=CENTER).grid(row=9, column=5)
    Button(main_w, text='play', command=send_coord).grid(row=11, column=3)
    Button(main_w, text='quit', command=window.quit).grid(row=11, column=6)
    return ret


user_input = set_input(window)


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


def cenvas_field(w, pieces, player=-1):
    canvas = Canvas(w, width=800, height=800)
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


def main_windows():
    global window, dict_pieces
    window.title("Chess by Popino et Lulu")
    window.mainloop()

