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
    3: pygame.image.load('textures/minecraftTextures1.png'),
    4: pygame.image.load('textures/minecraftTextures2.png'),
    5: pygame.image.load('textures/minecraftTextures3.png'),
    6: pygame.image.load('textures/minecraftTextures4.png'),
    7: pygame.image.load('textures/minecraftTextures5.png'),
    8: pygame.image.load('textures/minecraftTextures6.png'),
    9: pygame.image.load('textures/minecraftTextures7.png'),
    1: pygame.image.load('textures/minecraftTextures8.png'),
    2: pygame.image.load('textures/minecraftTextures9.png'),
    12: pygame.image.load('textures/star.png'),
    }
# Posicion, tamaño y ubicacion del sprite en la carpeta
sprites1 = [
    [(400,80), 10, './enemies/fire.png'],
    [(400,400), 10, './enemies/mob1.png'],
    [(400,200), 10, './enemies/mob2.png'],
]
sprites2 = [
    [(100,300), 10, './enemies/mob2.png'],
    [(400,400), 10, './enemies/fire2.png'],
    [(400,100), 10, './enemies/fire.png'],
]
sprites3 = [
    [(400,80), 10, './enemies/fire.png'],
    [(100,400), 10, './enemies/mob3.png'],
    [(400,200), 10, './enemies/mob2.png'],
]

SPRITES = [
    sprites1,
    sprites2,
    sprites3,
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