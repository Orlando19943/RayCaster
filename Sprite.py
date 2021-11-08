import pygame
from math import cos, sin, pi, atan2
SPRITE_BACKGROUND = (152, 0, 136, 255)

class Sprite(object):
    def __init__(self, position, size, sprite):
        self.position = [i/2 for i in position]
        self.size = size
        self.sprite = pygame.image.load(sprite)
        self.hitEnemy = False
        
    def drawSprite(self, player, screenSize, zbuffer, screen):
        # Pitagoras
        spriteDist = ((player.position[0] - self.position[0]) ** 2 + (player.position[1] - self.position[1]) ** 2) ** 0.5

        # Angulo
        spriteAngle = atan2(self.position[1] - player.position[1], self.position[0] - player.position[0]) * 180 / pi

        #Tamaño del sprite
        aspectRatio = self.sprite.get_width() / self.sprite.get_height()
        spriteHeight = (screenSize[1] / spriteDist) * self.size
        spriteWidth = spriteHeight * aspectRatio

        # Buscar el punto inicial para dibujar el sprite
        angleDif = (spriteAngle - player.angle * 180/pi) % 360
        angleDif = (angleDif - 360) if angleDif > 180 else angleDif
        startX = angleDif * screenSize[0] / player.fov
        startX += (screenSize[0] /  2) - (spriteWidth  / 2)
        startY = (screenSize[1] /  2) - (spriteHeight / 2)
        startX = int(startX)
        startY = int(startY)
        self.hitEnemy = False
        for x in range(startX, startX + int(spriteWidth)):
            if (0 < x < screenSize[0]) and zbuffer[x] >= spriteDist:
                for y in range(startY, startY + int(spriteHeight)):
                    tx = int((x - startX) * self.sprite.get_width() / spriteWidth )
                    ty = int((y - startY) * self.sprite.get_height() / spriteHeight )
                    texColor = self.sprite.get_at((tx, ty))
                    if texColor != SPRITE_BACKGROUND and texColor[3] > 128:
                        screen.set_at((x,y), texColor)

                        if y == screenSize[1] / 2:
                            zbuffer[x] = spriteDist
                            if x == screenSize[0] / 2:
                                self.hitEnemy = True
