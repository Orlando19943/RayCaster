import pygame
from RayCaster import Raycaster
from MainScreen import MainScreen

WIDTH = 500 
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF | pygame.HWACCEL )
minimapScreen = pygame.Surface((WIDTH, HEIGHT) )
start = MainScreen(screen,(WIDTH,HEIGHT))
play2 = False
while not play2:
    play = start.run()
    if play:
        game = Raycaster(screen,minimapScreen, (WIDTH,HEIGHT), pSize = (10,10), pPosition = [100, 100], pSpeed=1, pColor=(0,0,0))
        play2 = game.run()
    else: 
        play2 = True

pygame.quit()
