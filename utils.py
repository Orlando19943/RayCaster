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
    2: pygame.image.load('textures/BIGDOOR2.png'),
    3: pygame.image.load('textures/BIGDOOR3.png'),
    4: pygame.image.load('textures/BIGDOOR4.png'),
    5: pygame.image.load('textures/STARG3.png'),
    6: pygame.image.load('textures/STARGR2.png'),
    }
# Posicion, tamaño y ubicacion del sprite en la carpeta
sprites = [
    [(200,80), 25, './enemies/sprite1.png'],
    [(400,80), 25, './enemies/sprite1.png']
]

MAPS = {
    1: "./maps/map.txt",
    2: "./maps/map2.txt",
    3: "./maps/map3.txt",
}

MUSIC = [
    "./musica/sound1.mp3",
    "./musica/caminar1.mp3",
]
MUSIC2 = [
    "./musica/sound1.wav",
    "./musica/caminar1.wav",
]