import pygame
from pygame.constants import KEYDOWN
from Player import *
from Map import *
from utils import COLORS, wallTextures, sprites, MUSIC
from Pause import Pause
from Sprite import Sprite
class Raycaster(object):
    def __init__(self, screen,minimapScreen, size =(500,500), pSize = (10,10), pPosition = [100,100], pPositionI = [100,100], pSpeed=2, pColor=(0,0,0)):
        self.size = size
        self.map = Map(size)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 25)    
        self.font2 = pygame.font.SysFont("lucidabright", 30)    
        self.pPositionI = pPositionI
        self.pPosition = pPosition
        self.pSize = pSize
        self.pSpeed = pSpeed
        self.pColor = pColor
        self.actualMap = 1
        self.player = Player(self.pPosition,self.pSize,self.pSpeed, color = self.pColor)
        self.screen = screen
        self.minimapScreen = minimapScreen
        self.maps = None
        self.pause = False
        self.zbuffer = [float('inf') for z in range(size[0])]
        self.sprites = [Sprite(sprite[0],sprite[1],sprite[2]) for sprite in sprites]
        self.delta = 0
        self.wallTextures = []

    def fps(self):
        fps = str(int(self.clock.get_fps()))
        fps = self.font.render(fps, 1, pygame.Color("white"))
        return fps

    def drawRayCaster(self):
        for i in range(self.player.ray):
            id, dist, pdx, pdy, angle, tx = self.player.drawRay(i, self.map)
            x = self.player.position[0] + (pdx) * dist
            y = self.player.position[1] + (pdy) * dist
            """ if i == int(self.player.ray/2):
                pygame.draw.line(self.minimapScreen,self.player.color,(self.player.position),(x,y)) """
            rayWidth = int(( self.map.halfWidth/ self.player.ray))+1
            for column  in range(rayWidth):
                self.zbuffer[column  * (rayWidth-1) + column ] = dist
            x = int(( (i / self.player.ray) * self.map.halfWidth))
            h = (self.size[1]*self.map.blockHeight) / (dist*cos((angle-self.player.angle)))
            y = int((self.map.halfHeight-h) / 2)
            tex = wallTextures[int(id)]
            tex = pygame.transform.scale(tex, (tex.get_width() * rayWidth, int(h)))
            tx = int(tx * tex.get_width())
            self.screen.blit(tex, (x, y), (tx,0,rayWidth,tex.get_height()))
        sightRect = (int(self.size[0] / 2 - 2), int(self.size[1] / 2 - 2), 5,5 )
        for sprite in self.sprites:
            sprite.drawSprite(self.player, self.size, self.zbuffer, self.screen)
            self.screen.fill(pygame.Color('red') if sprite.hitEnemy else pygame.Color('white'), sightRect)

    def run(self):
        pygame.display.set_caption("RayCaster")
        run = 1
        level = self.font.render("Nivel: " + str(self.actualMap), 1, pygame.Color("black"))
        pygame.mouse.set_cursor(pygame.cursors.tri_left)
        pygame.mixer.init()
        pygame.mixer.music.load(MUSIC[0])
        pygame.mixer.music.play(-1) # If the loops is -1 then the music will repeat indefinitely.
        self.wallTextures = {i+2: wallTextures[i+2].convert() for i in range(len(wallTextures))}
        while run:
            next = self.player.movePlayer(pygame, self.map, 1)
            if next:
                self.actualMap += 1
                if self.actualMap == (len(MAPS) + 1):
                    run = 0
                    return False
                self.map = Map(self.size, actualMap = self.actualMap)
                self.player = Player([100,100],self.pSize,self.pSpeed, color = self.pColor)
                #self.player.drawPlayer(self.screen)
                level = self.font.render("Nivel: " + str(self.actualMap), 1, pygame.Color("black"))
            if self.map:
                # Techo
                self.screen.fill(COLORS[7], (0, 0,  int(self.size[0] ), int(self.size[1] / 2)))

                # Piso
                self.screen.fill(COLORS[8], (0, int(self.size[1] / 2),  int(self.size[0]), int(self.size[1] / 2)))
                #self.player.drawPlayer(self.screen)
                self.drawRayCaster()
                self.screen.fill(COLORS[1],(0,0,30,30))
                self.screen.blit(self.fps(), (0,0))
                self.map.drawMap(self.screen, pygame, self.minimapScreen, self.player, self.sprites)

            self.screen.blit(level, (self.size[0]-100,0))
            pygame.display.flip()
            self.delta = self.clock.tick(90)
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
                        