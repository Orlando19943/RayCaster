import pygame
from Player import *
from Map import *
from colors import COLORS
class MainScreen(object):
    def __init__(self, size =(500,500), image = None):
        pygame.init()
        self.image = pygame.image.load(image)
        self.size = size
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 25)
        self.centerX = int(self.size[0]/2)
        self.centerY = int(self.size[1]/2)

    def fps(self):
        fps = str(int(self.clock.get_fps()))
        fps = self.font.render(fps, 1, pygame.Color("white"))
        return fps

    def run(self):
        screen = pygame.display.set_mode(self.size, pygame.DOUBLEBUF | pygame.HWACCEL )
        self.screen = screen
        screen.set_alpha(None)
        pygame.display.set_caption("Main Screen")
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.screen.blit(self.image, (0,0))
        run = 1
        enter = ((self.centerX - 70,self.centerY+20,100,30))
        quit = ((self.centerX - 70,self.centerY+60,100,30))
        enterText = self.font.render("Play", 1, pygame.Color("black"))
        quitText = self.font.render("Exit", 1, pygame.Color("black"))
        start = 0
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.centerX-70 <= mouse[0] <= self.centerX + 33 and self.centerY+58 <= mouse[1] <= self.centerY +90:
                        run = 0
                    if self.centerX-70 <= mouse[0] <= self.centerX + 33 and self.centerY+20 <= mouse[1] <= self.centerY +50:
                        run = 0
                        start = 1
                mouse = pygame.mouse.get_pos()
            if self.centerX-70 <= mouse[0] <= self.centerX + 33 and (self.centerY+58 <= mouse[1] <= self.centerY +90 or self.centerY+20 <= mouse[1] <= self.centerY +50):
                pygame.mouse.set_cursor(pygame.cursors.broken_x)
            else:
                pygame.mouse.set_cursor(pygame.cursors.tri_left)
            screen.fill(COLORS[1],(0,0,30,30))
            screen.blit(self.fps(), (0,0))
            screen.fill(COLORS[7], enter)
            screen.blit(enterText, (self.centerX-40,self.centerY+20))
            screen.fill(COLORS[7], quit)
            screen.blit(quitText, (self.centerX-40,self.centerY+60))
            self.clock.tick(60)
            pygame.display.update()

        pygame.quit()
        return start