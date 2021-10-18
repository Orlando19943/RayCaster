from colors import COLORS, wallTextures
from math import pi, cos, sin
class Map(object):
    def __init__(self, file,size, blockSize = 40, wallheight = 40):
        self.file = file
        self.map = []
        self.blockSize = blockSize
        self.wallheight = wallheight
        self.halfWidth = int(size[0]/2)
        self.halfHeight = int(size[1])
        self.maxDistance = 300
        self.limitDistance = self.maxDistance * 0.6
        self.load_map()

    def load_map(self):
        if self.file:
            with open(self.file) as file:
                    for line in file.readlines():
                        self.map.append( list(line.rstrip()))

    def drawBlock(self, x, y, id, screen, pygame):
        screen.fill(COLORS[int(id)], (x,y, self.blockSize, self.blockSize))
        #tex = wallTextures[id]
        #tex = pygame.transform.scale(tex, (self.blocksize, self.blocksize) )
        #rect = tex.get_rect()
        #rect = rect.move((x,y))
        #screen.blit(tex, rect)

    def drawMap(self, screen, pygame):
        for x in range(0,self.halfWidth,self.blockSize):
            for y in range(0,self.halfHeight,self.blockSize):
                i = int(x/self.blockSize)
                j = int(y/self.blockSize)
                if j < len(self.map):
                    if i < len(self.map[j]):
                        if self.map[j][i] != ' ':
                            self.drawBlock(x, y, self.map[j][i], screen, pygame)
                        else:
                            self.drawBlock(x, y, 2, screen, pygame)
