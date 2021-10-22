from RayCaster import Raycaster
from MainScreen import MainScreen
from colors import COLORS
WIDTH = 800
HEIGHT = 400
MAP = "./map.txt"
MAINSCREEN = "./textures/mainScreen.jpg"
start = MainScreen((WIDTH,HEIGHT), image=MAINSCREEN)
play = start.run()
if play:
    game = Raycaster((WIDTH,HEIGHT), MAP, pColor=COLORS[1])
    game.run()