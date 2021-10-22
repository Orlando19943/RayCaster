from RayCaster import Raycaster
from MainScreen import MainScreen
from colors import COLORS, MAPS
WIDTH = 800 
HEIGHT = 400
MAINSCREEN = "./textures/mainScreen.jpg"
start = MainScreen((WIDTH,HEIGHT), image=MAINSCREEN)
play = start.run()
if play:
    game = Raycaster((WIDTH,HEIGHT), pColor=COLORS[1])
    game.run()