from RayCaster import *
from colors import COLORS
WIDTH = 800
HEIGHT = 400
LIMIT = False   # Esto sirve para activar la distancia máxima a la que puede llegar un rayo
MAP = "./map.txt"

game = Raycaster((WIDTH,HEIGHT), MAP, pColor=COLORS[1], limit = LIMIT)
game.run()