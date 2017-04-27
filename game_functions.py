import pygame
import sys


def check_events():
	#the escape hatch for the main game loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#the user clicked the red x. Get out of teh game
			sys.exit()


