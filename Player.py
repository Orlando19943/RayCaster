from math import pi, cos, sin, tan
from random import randint
from colors import COLORS
class Player(object):
    def __init__(self, position, size, speed = 100, color = (255,0,0), angle = 0, angularSpeed = 0.3, fov = 60, ray = 100):
        self.position = position
        self.speed = speed
        self.angularSpeed = angularSpeed
        self.size = size
        self.color = color
        self.angle = angle
        self.fov = fov
        self.ray = ray
        self.pdx = cos(self.angle) * self.speed
        self.pdy = sin(self.angle) * self.speed
        self.pdx2 = cos(self.angle + pi/2) * self.speed
        self.pdy2 = sin(self.angle + pi/2) * self.speed

    def drawPlayer(self, screen):
        rect = (self.position[0] - 2,self.position[1] - 2,self.size[0],self.size[1])
        screen.fill(self.color,rect)

    def drawRay(self, ray, map, limit):
        dist = 0
        angle =(self.angle*180/pi) -(self.fov/2) + (self.fov*ray/self.ray)
        rads = angle *pi/180
        pdx = cos(rads)
        pdy = sin(rads)
        x = self.position[0]
        y = self.position[1]
        while True:
            dist+=1
            x += pdx
            y += pdy
            i = int((x)/map.blockSize)
            j = int((y)/map.blockSize)
            if (map.map[j][i] != ' '):
                hitX = x - i * map.blockSize
                hitY = y - j * map.blockSize
                hit = 0
                if 1 < hitX < map.blockSize-1:
                    if hitY < 1:
                        hit = map.blockSize - hitX
                    elif hitY >= map.blockSize-1:
                        hit = hitX
                elif 1 < hitY < map.blockSize-1:
                    if hitX < 1:
                        hit = hitY
                    elif hitX >= map.blockSize-1:
                        hit = map.blockSize - hitY
                tx = hit/map.blockSize
                return map.map[j][i], dist, pdx, pdy, rads, tx
    def movePlayer(self, move, pygame, map):
        x = self.position[0]
        y = self.position[1]
        if (move == pygame.K_s) or (move == pygame.K_DOWN):
            x -=self.pdx * self.speed
            y -=self.pdy * self.speed
        if (move == pygame.K_w)  or (move == pygame.K_UP):
            x +=self.pdx * self.speed
            y +=self.pdy * self.speed
        if (move == pygame.K_d)  or (move == pygame.K_RIGHT):
            x +=self.pdx2 * self.speed
            y +=self.pdy2 * self.speed
        if (move == pygame.K_a)  or (move == pygame.K_LEFT): 
            x -=self.pdx2 * self.speed
            y -=self.pdy2 * self.speed
        if (move == pygame.K_q): 
            self.angle -= self.angularSpeed
            if self.angle < 0:
                self.angle +=2*pi 
            self.pdx = cos(self.angle) * self.speed
            self.pdy = sin(self.angle) * self.speed
            self.pdx2 = cos(self.angle + pi/2) * self.speed
            self.pdy2 = sin(self.angle + pi/2) * self.speed
        if (move == pygame.K_e):
            self.angle += self.angularSpeed
            if self.angle > (2*pi):
                self.angle -=2*pi 
            self.pdx = cos(self.angle) * self.speed
            self.pdy = sin(self.angle) * self.speed
            self.pdx2 = cos(self.angle + pi/2) * self.speed
            self.pdy2 = sin(self.angle + pi/2) * self.speed
        i = int((x+2)/map.blockSize)
        j = int((y+2)/map.blockSize)
        if map.map[j][i] == ' ':
            self.position[0] = x
            self.position[1] = y