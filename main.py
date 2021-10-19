from RayCaster import Raycaster
from MainScreen import MainScreen
from colors import COLORS
WIDTH = 800
HEIGHT = 400
LIMIT = False   # Esto sirve para activar la distancia máxima a la que puede llegar un rayo
MAP = "./map.txt"
MAINSCREEN = "./textures/mainScreen.jpg"
start = MainScreen((WIDTH,HEIGHT), image=MAINSCREEN)
if True:
    game = Raycaster((WIDTH,HEIGHT), MAP, pColor=COLORS[1], limit = LIMIT)
    game.run()