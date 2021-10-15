
class Player(object):
    def __init__(self, position, size, speed, color = (255,0,0)):
        self.position = position
        self.speed = speed
        self.size = size
        self.color = color

    def drawPlayer(self, screen):
        rect = (self.position[0],self.position[1],self.size[0],self.size[1])
        screen.fill(self.color,rect)

    def movePlayer(self, move, pygame):
        if move == pygame.K_s:
            self.position[1] += 1 * self.speed
        if move == pygame.K_w:
            self.position[1] -= 1 * self.speed
        if move == pygame.K_d:
            self.position[0] += 1 * self.speed
        if move == pygame.K_a:
            self.position[0] -= 1 * self.speed
