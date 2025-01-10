# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, constants, circleshape, player
from constants import *
from player import *

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
	my_player = Player(x, y) 

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		
		screen.fill((0,0,0), rect=None, special_flags=0)
		my_player.draw(screen)
		dt = clock.tick(60) / 1000
		pygame.display.flip()


if __name__ == "__main__":
	main()
