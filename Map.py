from utils import wallTextures, MAPS
class Map(object):
    def __init__(self,size, blockSize = 40, wallheight = 40, actualMap = 1):
        self.actualMap = actualMap
        self.file = MAPS[self.actualMap]
        self.size = size
        self.map = []
        self.blockSize = blockSize
        self.blockWidth = int(size[0]/20)
        self.blockHeight = int(size[1]/20)
        self.wallheight = wallheight
        self.halfWidth = int(size[0])
        self.halfHeight = int(size[1])
        self.maxDistance = 300
        self.minimapHeight = int(size[1]/5)
        self.minimapWidth = int(size[0]/5)
        self.limitDistance = self.maxDistance * 0.6
        self.load_map()

    def load_map(self):
        if self.file:
            with open(self.file) as file:
                    for line in file.readlines():
                        self.map.append( list(line.rstrip()))

    def drawBlock(self, x, y, id, pygame, minimapScreen):
        if id == "a":
            tex = wallTextures[12]
            tex = pygame.transform.scale(tex, (self.blockWidth*2,self.blockHeight*2) )
            rect = tex.get_rect()
            rect = rect.move((x*2,y*2))
            minimapScreen.blit(tex, rect)
            return
        elif id == "b":
            return
        elif 1<=int(id)<=9:
            tex = wallTextures[int(id)]
            tex = pygame.transform.scale(tex, (self.blockWidth*2,self.blockHeight*2) )
            rect = tex.get_rect()
            rect = rect.move((x*2,y*2))
            minimapScreen.blit(tex, rect)

    def drawMap(self, screen, pygame, minimapScreen, player, sprites):
        minimapScreen.fill(pygame.Color("gray"))
        for x in range(0,self.halfWidth,self.blockWidth):
            for y in range(0,self.halfHeight,self.blockHeight):
                i = int(x/self.blockWidth)
                j = int(y/self.blockHeight)
                if j < len(self.map):
                    if i < len(self.map[j]):
                        if self.map[j][i] != ' ':
                            self.drawBlock(x, y, self.map[j][i], pygame, minimapScreen)
                        else:
                            self.drawBlock(x, y, "b", pygame, minimapScreen)
        rect = (int(player.position[0] - 4)*2, int((player.position[1]) - 4)*2, 20,20)
        minimapScreen.fill(pygame.Color('black'), rect )
        for sprite in sprites:
            rect = ((sprite.position[0] - 4)*2, (sprite.position[1] - 4)*2, 20,20)
            minimapScreen.fill(pygame.Color('red'), rect )
        minimapScreen = pygame.transform.scale(minimapScreen, (self.minimapWidth,self.minimapHeight) )
        screen.blit(minimapScreen, (self.size[0] - self.minimapWidth,self.size[1] - self.minimapHeight))