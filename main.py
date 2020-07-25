import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, sys
from pygame.locals import *
import time
import random

pygame.init()


class Hangman:
	width = 700
	height = 480
	letters = {'a':False, 'b':False, 'c':False, 'd':False, 'e':False, 'f':False, 'g':False, 'h':False, 'i':False, 
					'j':False, 'k':False, 'l':False, 'm':False, 'n':False, 'o':False, 'p':False, 'q':False, 'r':False, 
					's':False, 't':False, 'u':False, 'v':False, 'w':False, 'x':False, 'y':False, 'z':False  }
	
	backgroundColor = (255,255,255) #white
	circleColor = (255,120,0) # random
	fontColor = (0,0,0) #black

	win = pygame.display.set_mode((width, height))
	font = pygame.font.SysFont('comicsans', 30)

	words = ["one", 'two', 'three', 'four', 'five', 'six']
	hangman = 0
	guess = ""

	def __init__(self):
		self.font_render = []
		for i in range(26):
			self.font_render.append(self.font.render(chr(i+65), 1, self.fontColor))
		self.font_render.append(self.font.render("_", 1, self.fontColor))

		self.image_render = []
		for i in range(1,7):
			self.image_render.append(pygame.image.load("Images/{}.png".format(i)))

	def drawBlank(self, word):
		for i in range(len(word)):
			self.win.blit(self.font_render[26], (50+i*30,420))
		self.win.blit(self.image_render[0],(280,160))


	def drawCircles(self):
		for i in range(13):
			pygame.draw.circle(self.win, self.circleColor, (i*50+50,40), 20)
			if(self.letters[chr(i+97)] == False):
				self.win.blit(self.font_render[i], (i*50+43, 30))
			
			pygame.draw.circle(self.win, self.circleColor, (i*50+50,95), 20)
			if(self.letters[chr(i+110)] == False):
				self.win.blit(self.font_render[i+13], (i*50+43, 85))

	def drawWord(self,word):
		for i in range(len(word)):
			if(self.letters[word[i]]==False):
				self.win.blit(self.font_render[26], (50+i*30,420))
			else:
				self.win.blit(self.font_render[ord(word[i])-97], (50+i*30,420))

	def letterPressed(self, letter, word):
		if(self.letters[letter] == True):
			return
		self.letters[letter] = True
		if(letter not in word):
			self.hangman += 1
			pygame.draw.rect(self.win, self.backgroundColor, (280,160,200,250))
			self.win.blit(self.image_render[self.hangman],(280,160))
			if(self.hangman == 5):
				print("you loose")
		else:
			self.guess+=letter
			if(self.guess==word):
				print("you win")

	def play(self):
		self.win.fill(self.backgroundColor)
		word = random.choice(self.words)
		print(word)
		self.drawBlank(word)
		while(True):
			pygame.display.set_caption("Hangman")
			for event in pygame.event.get():
					#quit game if user clicks the cross
					if(event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
						pygame.quit()
						sys.exit()
					elif(event.type == KEYDOWN):
						if(event.key == K_a):
							self.letterPressed('a', word)
						elif(event.key == K_b):
							self.letterPressed('b', word)
						elif(event.key == K_c):
							self.letterPressed('c', word)
						elif(event.key == K_d):
							self.letterPressed('d', word)
						elif(event.key == K_e):
							self.letterPressed('e', word)
						elif(event.key == K_f):
							self.letterPressed('f', word)
						elif(event.key == K_g):
							self.letterPressed('g', word)
						elif(event.key == K_h):
							self.letterPressed('h', word)
						elif(event.key == K_i):
							self.letterPressed('i', word)
						elif(event.key == K_j):
							self.letterPressed('j', word)
						elif(event.key == K_k):
							self.letterPressed('k', word)
						elif(event.key == K_l):
							self.letterPressed('l', word)
						elif(event.key == K_m):
							self.letterPressed('m', word)
						elif(event.key == K_n):
							self.letterPressed('n', word)
						elif(event.key == K_o):
							self.letterPressed('o', word)
						elif(event.key == K_p):
							self.letterPressed('p', word)
						elif(event.key == K_q):
							self.letterPressed('q', word)
						elif(event.key == K_r):
							self.letterPressed('r', word)
						elif(event.key == K_s):
							self.letterPressed('s', word)
						elif(event.key == K_t):
							self.letterPressed('t', word)
						elif(event.key == K_u):
							self.letterPressed('u', word)
						elif(event.key == K_v):
							self.letterPressed('v', word)
						elif(event.key == K_w):
							self.letterPressed('w', word)
						elif(event.key == K_x):
							self.letterPressed('x', word)
						elif(event.key == K_y):
							self.letterPressed('y', word)
						elif(event.key == K_z):
							self.letterPressed('z', word)
						
			self.drawCircles()
			self.drawWord(word)
			pygame.display.update()


game = Hangman()
game.play()	
