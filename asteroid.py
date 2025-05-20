import circleshape, constants, random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):    # don't touch this line
        super().__init__(x, y, radius)  # something I thought might work


    def draw(self, screen):
        pygame.draw.circle(screen, (155,255,255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        new_angle_a = self.velocity.rotate(random_angle)
        new_angle_b = self.velocity.rotate(-random_angle)
        
        starting_postion = self.position.copy()

        new_asteroid_a = Asteroid(0,0, (self.radius - ASTEROID_MIN_RADIUS))
        new_asteroid_a.position = starting_postion.copy()
        new_asteroid_a.velocity = new_angle_a * 1.2

        new_asteroid_b = Asteroid(0,0, (self.radius - ASTEROID_MIN_RADIUS))
        new_asteroid_b.position = starting_postion
        new_asteroid_b.velocity = new_angle_b




        