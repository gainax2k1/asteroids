import circleshape, constants
from constants import *
from circleshape import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) # L5 CH2 step 3
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2) # L5 CH2 step 5
 
    # in the player class
    # DONT TOUCH BELOW THIS
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]