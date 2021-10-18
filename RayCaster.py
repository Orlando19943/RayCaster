import pygame
from Player import *
from Map import *
from colors import COLORS
class Raycaster(object):
    def __init__(self, size =(500,500), map = None, pSize = (10,10), pPosition = [50,100], pSpeed=2, pColor=(0,0,0), limit = False):
        pygame.init()
        self.size = size
        self.map = Map(map,size)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 25)
        self.player = Player(pPosition,pSize,pSpeed, color = pColor)
        self.screen = None
        self.limit = limit
    def fps(self):
        fps = str(int(self.clock.get_fps()))
        fps = self.font.render(fps, 1, pygame.Color("white"))
        return fps

    def drawRayCaster(self):
        for i in range(self.player.ray):
            id, dist, pdx, pdy, angle = self.player.drawRay(i, self.map, self.limit)
            x = self.player.position[0] + (pdx) * dist
            y = self.player.position[1] + (pdy) * dist
            pygame.draw.line(self.screen,self.player.color,(self.player.position),(x,y))
            rayWidth = int(( self.map.halfWidth/ self.player.ray))
            x = self.map.halfWidth + int(( (i / self.player.ray) * self.map.halfWidth))
            # Esto lo hago porque en algunas ocasiones, deja algunos espacios entre cada columna 
            if i < self.player.ray:
                x2 = self.map.halfWidth + int(( ((i+1) / self.player.ray) * self.map.halfWidth))
                if (x +rayWidth) != x2:
                    rayWidth += 1
            h = self.size[1] / (dist*cos((angle-self.player.angle))) * self.map.wallheight
            y = int((self.map.halfHeight-h) / 2)
            color_k = 1-min(1,dist/self.map.maxDistance)
            color = [i*color_k for i in COLORS[int(id)]]
            self.screen.fill(color, (x, y, rayWidth, h))

    def run(self):
        screen = pygame.display.set_mode(self.size, pygame.DOUBLEBUF | pygame.HWACCEL )
        self.screen = screen
        screen.set_alpha(None)
        pygame.display.set_caption("RayCaster")
        run = 1
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.player.movePlayer(event.key, pygame, self.map)
                if event.type == pygame.QUIT:
                    run = 0
            screen.fill(COLORS[5])
            # Techo
            screen.fill(COLORS[7], (int(self.size[0] / 2), 0,  int(self.size[0] / 2), int(self.size[1] / 2)))

            # Piso
            screen.fill(COLORS[8], (int(self.size[0] / 2), int(self.size[1] / 2),  int(self.size[0] / 2), int(self.size[1] / 2)))
            self.map.drawMap(screen, pygame)
            self.player.drawPlayer(screen)
            screen.fill(COLORS[1],(0,0,30,30))
            screen.blit(self.fps(), (0,0))
            self.drawRayCaster()
            self.clock.tick(60)
            pygame.display.update()

        pygame.quit()