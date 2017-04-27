#we have access to pygame because we installed it
#$ pip install pygame
#must install pygame because it is not part of core
import pygame
#import sys module from core so we can exit the program
# import sys
from random import randint
from player import Player
from game_functions import check_events

#core game functionality and loop
def run_game():
	#init all pygame stuff
	pygame.init()
	#setup a tuple for screen size, (x,y)
	screen_size = (1000, 800)
	#set tuple for bg color
	background_color = (225,75,111)
	#create a pygame to use
	screen = pygame.display.set_mode(screen_size)
	#set a caption on the terminal window
	pygame.display.set_caption("3rd person shooter")

	the_player = Player(screen)

	#/////////////////////////////
	#////////MainGAMELoop////////
	#///////////////////////////
	while 1:
		# background_color = (randint(0,255), randint(0,255), randint(0,255))
		screen.fill(background_color)

		check_events()

		#draw the player
		the_player.draw_me()
		#clear screen for next time through tthe loop
		pygame.display.flip()

run_game()