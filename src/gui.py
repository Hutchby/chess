# TODO: fix trouble with coord (0,0) should be bottom left or top right depending on newt player
# rendu graphique pour le moment ta fonction de rendu

from tkinter import *
from src.rules import * # for itoa
import src.game
import src.pieces

window = Tk()
m = PanedWindow(window, orient=VERTICAL)
p = PanedWindow(m, orient=HORIZONTAL)
fclick = ()
first_click = (-1, -1)
intput_row = 10


def set_buttons(main_w):
    ret = []
    for i in range(0, 8):
        ret.append([])
        for j in range(0, 8):
            if (i + j) % 2 == 0:
                color_bg = "DarkOrange4"
            else:
                color_bg = "white"
            ret[i].append(Button(main_w, text='_', command=lambda a=i, b=j: onbuttonclick(a+1, b+1), bg=color_bg))
            ret[i][j].config(height=3, width=6)
            ret[i][j].grid(row=8 - j, column=i + 1)
    return ret

board = set_buttons(window)


def refresh_board():
    global board, window

    print("rfresh for p: " + str(src.game.player))
    # print(dict_pieces.keys())
    if src.game.player == -1:
        col = 'red'
    else:
        col = 'blue'
    for i in range(0, 8):
        if src.game.player == -1:
            Label(window, text=i+1, background='white', anchor=CENTER).grid(row=0, column=i+1)
            Label(window, text=i+1, background='white', anchor=CENTER).grid(row=i+1, column=0)
        else:
            Label(window, text=i+1, background='white', anchor=CENTER).grid(row=0, column=8 - i)
            Label(window, text=i+1, background='white', anchor=CENTER).grid(row=8 - i, column=0)
        for j in range(0, 8):
            board[i][j].config(text='')
    # board[1][9].config(text="Turn: %d" % (player,), fg=col)
    Label(window, text="Turn: %d" % (src.game.player,), background='white', fg=col, anchor=CENTER).grid(row=intput_row, column=1)
    for pos in src.game.dict_pieces.keys():
        if src.pieces.dict_pieces[pos].player == -1:
            col = 'red'
        else:
            col = 'blue'
        if src.game.player == -1:
            board[pos[0] - 1][pos[1] - 1].config(text=src.pieces.dict_pieces[pos].symbol, fg=col)
        else:
            board[8 - pos[0]][8 - pos[1]].config(text=src.pieces.dict_pieces[pos].symbol, fg=col)


def onbuttonclick(i, j):
    global fclick
    print("click :", i, j)
    if src.game.player == 1:
        i = 9 - i
        j = 9 - j
    if len(fclick) == 0:
        if src.game.there_is_something(src.pieces.dict_pieces, i, j):
            fclick = (i, j)
            print(src.pieces.dict_pieces[fclick].list_move(fclick, src.pieces.dict_pieces))

    else:
        src.game.turn(fclick, (i, j))
        fclick = ()
        refresh_board()


def send_coord():
    global dict_pieces, player
    print("test")
    # dict_pieces[3, 3] = Bishop(1)
    move = []
    for i in range(0, 4):
        move.append(user_input[i].get())
    print(move)

    # turn()
    refresh_board()
    return move


def set_input(main_w):
    ret = [Entry(main_w, width=2), Entry(main_w, width=2), Entry(main_w, width=2), Entry(main_w, width=2)]
    ret[0].grid(row=intput_row, column=3)
    ret[1].grid(row=intput_row, column=4)
    ret[2].grid(row=intput_row, column=6)
    ret[3].grid(row=intput_row, column=7)
    if src.game.player == -1:
        col = 'red'
    else:
        col = 'blue'
    Label(main_w, text="Turn: %d" % (src.game.player,), background='white', fg=col, anchor=CENTER).grid(row=intput_row, column=1)
    Label(main_w, text='from', background='white', anchor=CENTER).grid(row=intput_row, column=2)
    Label(main_w, text='to', background='white', anchor=CENTER).grid(row=intput_row, column=5)
    Button(main_w, text='play', command=send_coord).grid(row=intput_row+2, column=3)
    Button(main_w, text='quit', command=window.quit).grid(row=intput_row+2, column=6)
    return ret


user_input = set_input(window)


def main_windows():
    global window, dict_pieces
    window.title("Chess by Paul Halbeher et Lucien Ricimello")
    window.mainloop()
