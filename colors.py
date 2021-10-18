import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
PURPLE = (131,12,229)
FOG = (194,211,211)
BLACK2 = (22,22,22)
COLORS = {
    1: BLACK,
    2: WHITE,
    3: PURPLE,
    4: RED,
    5: BLUE,
    6: GREEN,
    7: FOG,
    8: BLACK2,
}

wallTextures = {
    3: pygame.image.load('textures/wall1.png'),
    4: pygame.image.load('textures/wall2.png'),
    5: pygame.image.load('textures/wall3.png'),
    6: pygame.image.load('textures/wall4.png'),
    }