import circleshape, constants, shot
from constants import *
from circleshape import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) # L5 CH2 step 3
        self.rotation = 0
        self.cooldown_timer = 0 # timer for shots

    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2) # L5 CH2 step 5
 
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.cooldown_timer > 0:
            return
        else:
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN
            new_shot = Shot(1,1)
            new_shot.position = self.position.copy()
            new_shot.velocity = pygame.Vector2(0,1)
            new_shot.velocity = new_shot.velocity.rotate(self.rotation) # .rotate returns a value, doesn't modify itself
            new_shot.velocity *= PLAYER_SHOOT_SPEED


    # in the player class
    # DONT TOUCH BELOW THIS
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update(self, dt):
        self.cooldown_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        