import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, sys
from pygame.locals import *

import play

pygame.init()

width = 700
height = 480	
win = pygame.display.set_mode((width, height))
fnt = pygame.font.SysFont('comicsans', 30)
FNT = pygame.font.SysFont('comicsans', 50)
	

term_x = [250, 450]
term_y = [200, 250, 300, 350]

easy_words = ['cycle', 'fake', 'funny', 'injury', 'lucky', 'puppy', 'queue', 'vodka', 'wave', 'wheel']
medium_words = ['abrupt', 'equip', 'galaxy', 'gossip', 'pixel', 'luxury', 'strength', 'zombie']
hard_words = ['recitation', 'valuation', 'testimony', 'awkward', 'microwave', 'rhythm', 'twelfth', 'xylophone']

while(True):
	win.fill((197, 227, 236))
	win.blit(FNT.render("Welcome to Hangman", 0,(0,0,0)),(170, 100))  	
	options = ["EASY", "MEDIUM", "HARD"]
	text = [fnt.render(options[i], 0, (0,0,0)) for i in range(3)]
	x = [200, 400]
	y = [200, 250, 300,350]
	for i in range(4) :
		pygame.draw.line(win, (0,0,0), (term_x[0], term_y[i]), (term_x[1], term_y[i]))
	for i in range(2) :
		pygame.draw.line(win, (0,0,0), (term_x[i], 200), (term_x[i], 350))

	for i in range(3) :
		win.blit(text[i], (315, y[i] + 15))  
	pygame.display.update()
	for event in pygame.event.get() :
		#if quit detected
		if(event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE) ):
			pygame.quit()
			sys.exit()         
		#detecting the mouseclick and checking which button was selected (and breaking out from 2 loops)
		elif( event.type == MOUSEBUTTONDOWN ):
			x, y = pygame.mouse.get_pos()
			if( 250 < x < 450 and y > 200):
				if( y < 250 ):
					play.Hangman(easy_words)
				elif( y < 300 ):
					play.Hangman(medium_words)
				elif( y < 350 ):
					play.Hangman(hard_words)
		elif( event.type == KEYDOWN ):
			if(event.key == K_e):
				play.Hangman(easy_words)
			elif(event.key == K_m):
				play.Hangman(medium_words)
			elif(event.key == K_h):
				play.Hangman(hard_words)
