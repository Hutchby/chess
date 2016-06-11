# rendu graphique pour le moment ta fonction de rendu

from tkinter import *

def afficherTerrain(listPiece):
   window = Tk()
   window.title("Plateau de jeu")
   canvas = Canvas(window, width=800, height=800)
   canvas.create_text(45, 755, text = '0')
   canvas.create_text(755, 675, text = '0')

   for i in range(1, 8):
       canvas.create_line(90 * i, 0, 90 * i, 720)
       canvas.create_text(i * 90 + 45, 755, text = i)
       canvas.create_text(755, 720 - i * 90 - 45, text = i)
       canvas.create_line(0, 90 * i, 720, 90 * i)

   for piece in listPiece:
       if (piece.player == 1):
           color = "blue"
       else:
           color = "red"
       canvas.create_text(piece.position[0] * 90 + 45, 720 - piece.position[1] * 90 - 45, text = piece.category, fill= color)

   canvas.pack()
   window.mainloop()

