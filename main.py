from RayCaster import *

WIDTH = 1000
HEIGHT = 500
BLACK = (0,0,0)
WHITE = (255,255,255)
MAP = "./map.txt"

game = Raycaster((WIDTH,HEIGHT), MAP, pColor=BLACK)
game.run()