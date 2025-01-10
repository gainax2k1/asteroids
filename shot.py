import circleshape, constants
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y):    # don't touch this line
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = 0


    def draw(self, screen):
        pygame.draw.circle(screen, (155,255,255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)



        