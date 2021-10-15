from math import pi, cos, sin
class Player(object):
    def __init__(self, position, size, speed = 5, color = (255,0,0), angle = 0):
        self.position = position
        self.speed = speed
        self.size = size
        self.color = color
        self.angle = angle
        self.pdx = cos(self.angle) * self.speed
        self.pdy = sin(self.angle) * self.speed

    def drawPlayer(self, screen):
        rect = (self.position[0],self.position[1],self.size[0],self.size[1])
        screen.fill(self.color,rect)

    def drawRay(self, screen, pygame):
        rect = (self.position[0],self.position[1],self.pdx,self.pdy)
        pygame.draw.line(screen,self.color,(self.pdx,self.pdy),(self.position[0],self.position[1]))

    def movePlayer(self, move, pygame):
        if move == pygame.K_w:
            self.position[0] -=self.pdx
            self.position[1] -=self.pdy
        if move == pygame.K_s:
            self.position[0] +=self.pdx
            self.position[1] +=self.pdy
        if move == pygame.K_d:
            self.angle += 0.1
            if self.angle < 0:
                self.angle -=2*pi 
            self.pdx = cos(self.angle) * self.speed
            self.pdy = sin(self.angle) * self.speed
        if move == pygame.K_a: 
            self.angle -= 0.1
            if self.angle < 0:
                self.angle +=2*pi 
            self.pdx = cos(self.angle) * self.speed
            self.pdy = sin(self.angle) * self.speed
