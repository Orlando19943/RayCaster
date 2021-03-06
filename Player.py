from math import pi, cos, sin
class Player(object):
    def __init__(self, position, size, speed =0.01, color = (255,0,0), angle = 0, angularSpeed = 0.04, fov = 60, ray = 100):
        self.position = [i/2 for i in position]
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

    def drawRay(self, ray, map):
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
            i = int((x)/map.blockWidth)
            j = int((y)/map.blockHeight)
            if (map.map[j][i] != ' ' and map.map[j][i] != "a"):
                hitX = x - i * map.blockWidth
                hitY = y - j * map.blockHeight
                hit = 0
                if 1 < hitX < map.blockWidth-1:
                    if hitY < 1:
                        hit = map.blockWidth - hitX
                    elif hitY >= map.blockHeight-1:
                        hit = hitX
                elif 1 < hitY < map.blockHeight-1:
                    if hitX < 1:
                        hit = hitY
                    elif hitX >= map.blockWidth-1:
                        hit = map.blockHeight - hitY
                tx = hit/map.blockWidth
                return map.map[j][i], dist, pdx, pdy, rads, tx
    def movePlayer(self, pygame, map, delta):
        key = pygame.key.get_pressed()
        x = self.position[0]
        y = self.position[1]
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            x -=self.pdx * self.speed * delta
            y -=self.pdy * self.speed * delta
        if key[pygame.K_w] or key[pygame.K_UP]:
            x +=self.pdx * self.speed * delta
            y +=self.pdy * self.speed * delta
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            x +=self.pdx2 * self.speed * delta
            y +=self.pdy2 * self.speed * delta
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            x -=self.pdx2 * self.speed * delta
            y -=self.pdy2 * self.speed * delta
        if key[pygame.K_q]:
            self.angle -= self.angularSpeed
            if self.angle < 0:
                self.angle +=2*pi 
            self.pdx = cos(self.angle) * self.speed * delta
            self.pdy = sin(self.angle) * self.speed * delta
            self.pdx2 = cos(self.angle + pi/2) * self.speed * delta
            self.pdy2 = sin(self.angle + pi/2) * self.speed * delta
        if key[pygame.K_e]:
            self.angle += self.angularSpeed
            if self.angle > (2*pi):
                self.angle -=2*pi 
            self.pdx = cos(self.angle) * self.speed * delta
            self.pdy = sin(self.angle) * self.speed * delta
            self.pdx2 = cos(self.angle + pi/2) * self.speed * delta
            self.pdy2 = sin(self.angle + pi/2) * self.speed * delta
        i = int((x)/map.blockWidth)
        j = int((y)/map.blockHeight)

        if map.map[j][i] == ' ' or map.map[j][i] == 'a':
            if map.map[j][i] == 'a':
                return True
            self.position[0] = x
            self.position[1] = y
            return False
        return False