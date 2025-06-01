import pygame
from constants import *
from player import *

def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	pygame.init()
	fps = pygame.time.Clock()
	dt = 0
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	# game loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		screen.fill("black")
		player.draw(screen)
		pygame.display.flip()
		dt = fps.tick(60) / 1000


if __name__ == "__main__":
	main()

# import the connect_database function
# and th edatabase_version variable
# from database.py into the current file
