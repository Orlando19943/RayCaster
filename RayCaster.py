import pygame
from pygame.constants import KEYDOWN
from Player import *
from Map import *
from colors import COLORS, wallTextures
from Pause import Pause
class Raycaster(object):
    def __init__(self, screen, size =(500,500), pSize = (10,10), pPosition = [50,100], pSpeed=2, pColor=(0,0,0)):
        self.size = size
        self.map = Map(size)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 25)    
        self.font2 = pygame.font.SysFont("lucidabright", 30)    
        self.pPosition = pPosition
        self.pSize = pSize
        self.pSpeed = pSpeed
        self.pColor = pColor
        self.actualMap = 1
        self.player = Player(self.pPosition,self.pSize,self.pSpeed, color = self.pColor)
        self.screen = screen
        self.maps = None
        self.pause = False
    def fps(self):
        fps = str(int(self.clock.get_fps()))
        fps = self.font.render(fps, 1, pygame.Color("white"))
        return fps

    def drawRayCaster(self):
        for i in range(self.player.ray):
            id, dist, pdx, pdy, angle, tx = self.player.drawRay(i, self.map)
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
            h = self.size[1] / (dist*cos((angle-self.player.angle)))
            h *= self.map.wallheight
            y = int((self.map.halfHeight-h) / 2)
            color_k = (1 - min(1, dist / self.map.maxDistance)) * 255
            tex = wallTextures[int(id)]
            tex = pygame.transform.scale(tex, (tex.get_width() * rayWidth, int(h)))
            #tex.fill((color_k,color_k,color_k), special_flags=pygame.BLEND_MULT)
            tx = int(tx * tex.get_width())
            self.screen.blit(tex, (x, y), (tx,0,rayWidth,tex.get_height()))

    def run(self):
        pygame.display.set_caption("RayCaster")
        run = 1
        level = self.font.render("Nivel: " + str(self.actualMap), 1, pygame.Color("black"))
        pygame.mouse.set_cursor(pygame.cursors.tri_left)
        while run:
            next = self.player.movePlayer(pygame, self.map)
            if next:
                self.actualMap += 1
                if self.actualMap == (len(MAPS) + 1):
                    run = 0
                    return False
                self.map = Map(self.size, actualMap = self.actualMap)
                self.player = Player([50,100],(10,10),2, color = self.pColor)
                self.player.drawPlayer(self.screen)
                level = self.font.render("Nivel: " + str(self.actualMap), 1, pygame.Color("black"))
            if self.map:
                # Techo
                self.screen.fill(COLORS[7], (int(self.size[0] / 2), 0,  int(self.size[0] / 2), int(self.size[1] / 2)))

                # Piso
                self.screen.fill(COLORS[8], (int(self.size[0] / 2), int(self.size[1] / 2),  int(self.size[0] / 2), int(self.size[1] / 2)))
                self.map.drawMap(self.screen, pygame)
                self.player.drawPlayer(self.screen)
                self.screen.fill(COLORS[1],(0,0,30,30))
                self.screen.blit(self.fps(), (0,0))
                self.drawRayCaster()

            self.screen.blit(level, (self.size[0]-100,0))
            pygame.display.flip()
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = 0
                    return True
                if  event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = Pause(self.screen, (self.size[0], self.size[1]))
                        start, close = pause.run()
                        if start == False:
                            run = 0
                            return False
                        elif close == False: 
                            return True
                        