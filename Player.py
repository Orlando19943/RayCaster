from math import pi, cos, sin, tan
from random import randint
from colors import COLORS
class Player(object):
    def __init__(self, position, size, speed = 5, color = (255,0,0), angle = 0, angularSpeed = 10, fov = 60, ray = 100):
        self.position = position
        self.speed = speed
        self.angularSpeed = angularSpeed
        self.size = size
        self.color = color
        self.angle = angle
        self.fov = fov
        self.ray = ray
        self.pdx = cos(self.angle) * self.angularSpeed
        self.pdy = sin(self.angle) * self.angularSpeed
        self.pdx2 = cos(self.angle + pi/2) * self.angularSpeed
        self.pdy2 = sin(self.angle + pi/2) * self.angularSpeed

    def drawPlayer(self, screen):
        rect = (self.position[0] - 2,self.position[1] - 2,self.size[0],self.size[1])
        screen.fill(self.color,rect)

    def drawRay(self, ray, map, limit):
        dist = 0
        angle =(self.angle*180/pi) -(self.fov/2) + (self.fov*ray/self.ray)
        rads = angle *pi/180
        pdx = cos(rads)
        pdy = sin(rads)
        while True:
            i = int((self.position[0]+2 + (pdx) * dist)/map.blockSize)
            j = int((self.position[1]+2 + (pdy) * dist)/map.blockSize)
            if map.map[j][i] == ' ':
                dist+=1
                if (dist == map.limitDistance) and(limit):
                    return 1, dist, pdx, pdy, rads
            elif (map.map[j][i] != ' '):
                return map.map[j][i], dist, pdx, pdy, rads

    def movePlayer(self, move, pygame, map):
        x = self.position[0]
        y = self.position[1]
        if (move == pygame.K_s) or (move == pygame.K_DOWN):
            x -=self.pdx
            y -=self.pdy
        if (move == pygame.K_w)  or (move == pygame.K_UP):
            x +=self.pdx
            y +=self.pdy
        if (move == pygame.K_d)  or (move == pygame.K_RIGHT):
            x +=self.pdx2
            y +=self.pdy2
        if (move == pygame.K_a)  or (move == pygame.K_LEFT): 
            x -=self.pdx2
            y -=self.pdy2
        if (move == pygame.K_q): 
            self.angle -= 0.2
            if self.angle < 0:
                self.angle +=2*pi 
            self.pdx = cos(self.angle) * self.speed
            self.pdy = sin(self.angle) * self.speed
            self.pdx2 = cos(self.angle + pi/2) * self.speed
            self.pdy2 = sin(self.angle + pi/2) * self.speed
        if (move == pygame.K_e):
            self.angle += 0.2
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
        

