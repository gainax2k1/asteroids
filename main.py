# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import circleshape
import player
import asteroid
import asteroidfield
import shot
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	print("Starting asteroids!")
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	x = (SCREEN_WIDTH / 2)
	y = (SCREEN_HEIGHT / 2) 

	asteroids = pygame.sprite.Group()
	updateable = pygame.sprite.Group() 
	drawable = pygame.sprite.Group()
	shot = pygame.sprite.Group() 

	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable)
	Shot.containers = (updateable, drawable)
	
	my_player = Player(x, y) 
	my_asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
	
		screen.fill((0,0,0), rect=None, special_flags=0)
		for thing_to_draw in drawable:
			thing_to_draw.draw(screen)

		dt = clock.tick(60) / 1000
		
		for thing_to_update in updateable:
			thing_to_update.update(dt)

		for things_to_colide in asteroids:
			if things_to_colide.check_collisions(my_player):
				print("Game over!")
				raise SystemExit


		pygame.display.flip()




if __name__ == "__main__":
	main()
