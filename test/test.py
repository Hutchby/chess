from src.gui import *


game_type = 1

if game_type != -1:
    print("there is a shortcut for the test, game_type = ", game_type)

while game_type < 0 or 2 < game_type:
    game_type = input("""What kind of game? (H:human, C: computer)
        # HvC: 0
        HvH: 1
        CvC: 2
    your choice: """)
    game_type = int(game_type)
    print(game_type, type(game_type))
main_windows()
