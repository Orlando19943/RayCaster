import pygame
from Player import *
from Map import *
from utils import COLORS
class MainScreen(object):
    def __init__(self, screen, size =(500,500)):
        pygame.init()
        self.image = pygame.image.load("./textures/mainScreen2.jpg")
        self.size = size
        self.font = pygame.font.SysFont("onyx", 30)
        self.fontTitle = pygame.font.SysFont("onyx", 45)
        self.centerX = int(self.size[0]/2)
        self.centerY = int(self.size[1]/2)
        self.option = True
        self.screen = screen

    def chooseOption(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            self.option = not self.option
        if key[pygame.K_w] or key[pygame.K_UP]:
            self.option = not self.option

    def run(self):
        pygame.display.set_caption("Main Screen")
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.screen.blit(self.image, (0,0))
        run = 1
        x = self.centerX*0.92
        quit = ((self.centerX - 60,self.centerY+60,100,30))
        enter = ((self.centerX - 60,self.centerY+20,100,30))
        enterText = self.font.render("Play", 1, pygame.Color("black"))
        title = self.fontTitle.render("RayCaster", 1, pygame.Color("black"))
        quitText = self.font.render("Exit", 1, pygame.Color("black"))
        start = 0
        self.screen.fill(COLORS[7], quit)
        self.screen.blit(title, (self.centerX*0.8,self.centerY*0.3))
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False
                    run = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.centerX-70 <= mouse[0] <= self.centerX + 33 and self.centerY+58 <= mouse[1] <= self.centerY +90:
                        run = 0
                    if self.centerX-70 <= mouse[0] <= self.centerX + 33 and self.centerY+20 <= mouse[1] <= self.centerY +50:
                        run = 0
                        start = 1
                if  event.type == pygame.KEYDOWN:
                    self.chooseOption()
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        start = self.option
                        run = 0
            mouse = pygame.mouse.get_pos()
            if self.centerX-60 <= mouse[0] <= self.centerX + 37 and (self.centerY+58 <= mouse[1] <= self.centerY +90 or self.centerY+20 <= mouse[1] <= self.centerY +50):
                pygame.mouse.set_cursor(pygame.cursors.broken_x)
            else:
                pygame.mouse.set_cursor(pygame.cursors.tri_left)
            if self.centerX-60 <= mouse[0] <= self.centerX + 37 and (self.centerY+20 <= mouse[1] <= self.centerY +50):
                self.option = True
            if self.centerX-60 <= mouse[0] <= self.centerX + 37 and (self.centerY+58 <= mouse[1] <= self.centerY +90):
                self.option = False
            # ------------------------------
            if self.option:
                self.screen.fill(COLORS[9], enter)
                self.screen.blit(enterText, (x,self.centerY+20))
            else:
                self.screen.fill(COLORS[7], enter)
                self.screen.blit(enterText, (x,self.centerY+20))
            if not self.option:
                self.screen.fill(COLORS[9], quit)
                self.screen.blit(quitText, (x,self.centerY+60))
            else:
                self.screen.fill(COLORS[7], quit)
                self.screen.blit(quitText, (x,self.centerY+60))
            pygame.display.update()

        return start