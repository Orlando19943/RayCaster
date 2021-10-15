import pygame
from Player import *
from Map import *
class Raycaster(object):
    def __init__(self, size =(500,500), map = None, pSize = (10,10), pPosition = [50,100], pSpeed=2, pColor=(0,0,0)):
        pygame.init()
        self.size = size
        self.map = Map(map,size)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 25)
        self.player = Player(pPosition,pSize,pSpeed, color = pColor)

    def fps(self):
        fps = str(int(self.clock.get_fps()))
        fps = self.font.render(fps, 1, pygame.Color("white"))
        return fps

    def run(self):
        screen = pygame.display.set_mode(self.size, pygame.DOUBLEBUF | pygame.HWACCEL )
        screen.set_alpha(None)
        pygame.display.set_caption("RayCaster")
        run = 1
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.player.movePlayer(event.key, pygame)
                if event.type == pygame.QUIT:
                    run = 0
            screen.fill(pygame.Color("gray"))
            self.map.drawMap(screen)
            self.player.drawPlayer(screen)
            screen.fill(pygame.Color("black"),(0,0,30,30))
            screen.blit(self.fps(), (0,0))
            self.clock.tick(60)
            pygame.display.update()

        pygame.quit()