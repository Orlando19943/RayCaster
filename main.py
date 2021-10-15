from RayCaster import *
from colors import COLORS
WIDTH = 800
HEIGHT = 400

MAP = "./map.txt"

game = Raycaster((WIDTH,HEIGHT), MAP, pColor=COLORS[5])
game.run()