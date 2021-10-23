import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
PURPLE = (131,12,229)
FOG = (142,144,143)
BLACK2 = (22,22,22)
BLACKT = (0,0,0, 128)
YELLOW = (242, 206, 24)
COLORS = {
    1: BLACK,
    2: WHITE,
    3: PURPLE,
    4: RED,
    5: BLUE,
    6: GREEN,
    7: FOG,
    8: BLACK2,
    9: YELLOW,
    10: BLACKT,
}

wallTextures = {
    2: pygame.image.load('textures/wall1.png'),
    3: pygame.image.load('textures/wall1.png'),
    4: pygame.image.load('textures/wall2.png'),
    5: pygame.image.load('textures/wall3.png'),
    6: pygame.image.load('textures/wall4.png'),
    }

MAPS = {
    1: "./maps/map.txt",
    2: "./maps/map2.txt",
    3: "./maps/map3.txt",
}