import pygame
from RayCaster import Raycaster
from MainScreen import MainScreen
WIDTH = 800 
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF | pygame.HWACCEL )
screen.set_alpha(None)
start = MainScreen(screen,(WIDTH,HEIGHT))
play2 = False
while not play2:
    play = start.run()
    if play:
        game = Raycaster(screen, (WIDTH,HEIGHT), pSize = (10,10), pPosition = [50,100], pSpeed=2, pColor=(0,0,0))
        play2 = game.run()
    else: 
        play2 = True

pygame.quit()