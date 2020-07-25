import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, sys
from pygame.locals import *
import time
import random

pygame.init()
pygame.mixer.init()

class Hangman:
	def __init__(self, words):
		self.width = 700
		self.height = 480
		self.letters = {'a':False, 'b':False, 'c':False, 'd':False, 'e':False, 'f':False, 'g':False, 'h':False, 'i':False, 
						'j':False, 'k':False, 'l':False, 'm':False, 'n':False, 'o':False, 'p':False, 'q':False, 'r':False, 
						's':False, 't':False, 'u':False, 'v':False, 'w':False, 'x':False, 'y':False, 'z':False  }
		
		self.backgroundColor = (197, 227, 236)
		self.circleColor = (199, 66, 97)
		self.fontColor = (0,0,0) #black

		self.win = pygame.display.set_mode((self.width, self.height))
		self.font = pygame.font.SysFont('comicsans', 30)

		self.hangman = 0
		self.wordLetterSet = set()
		self.numberOfLetters = 0
		self.gameFlag = True
		self.hintFlag = False
		self.words = words

		self.font_render = []
		for i in range(26):
			self.font_render.append(self.font.render(chr(i+65), 1, self.fontColor))
		self.font_render.append(self.font.render("_", 1, self.fontColor))

		self.image_render = []
		for i in range(1,8):
			self.image_render.append(pygame.image.load("Images/{}.png".format(i)))

		self.play()

	def initGame(self, word):
		for i in range(len(word)):
			self.win.blit(self.font_render[26], (50+i*30,420))
		self.win.blit(self.image_render[0],(280,160))
		for i in word:
			self.wordLetterSet.add(i)
		self.numberOfLetters = len(self.wordLetterSet)
		
	def renderScreen(self, text):
		self.win.fill(self.backgroundColor)
		fnt = pygame.font.SysFont("comicsans", 50)
		if(text=="Win"):
			self.win.blit(fnt.render("You "+text, True, (27, 48, 28)), (290,300))
			pygame.display.update()
			os.system('mpg123 -q --no-control '+"Audio/win.mp3")
		else:
			self.win.blit(fnt.render("You "+text, True, (161,0,0)), (260,300))
			pygame.display.update()
			os.system('mpg123 -q --no-control '+"Audio/loose.mp3")		
		self.win.blit(self.image_render[6], (330, 220))
		pygame.display.update()
		while True :
			for event in pygame.event.get() :
				if( event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE) ):
					pygame.quit()
					sys.exit()
				elif(event.type == MOUSEBUTTONDOWN ): # click on re button
					x, y = pygame.mouse.get_pos()
					if(330 < x < 394 and 220 < y < 284 ):
						return	
				elif(event.type==KEYDOWN and event.key in [K_b, K_BACKSPACE, K_RETURN]):
					return

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
			os.system('mpg123 -q --no-control '+"Audio/invalid.mp3")
			pygame.draw.rect(self.win, self.backgroundColor, (280,160,200,250))
			self.win.blit(self.image_render[self.hangman],(280,160))
			if(self.hangman == 5):
				self.renderScreen("Loose")
				self.gameFlag = False
		else:
			os.system('mpg123 -q --no-control '+"Audio/valid.mp3")
			self.wordLetterSet.remove(letter)
			if(len(self.wordLetterSet)==0):
				self.renderScreen("Win")
				self.gameFlag = False

	def play(self):
		self.win.fill(self.backgroundColor)
		word = random.choice(self.words)
		#print(word)
		self.initGame(word)
		while(self.gameFlag):
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
						elif(event.key == K_RETURN):
							self.hintFlag = not self.hintFlag
						
			if(self.hintFlag==True):
				self.win.blit(pygame.font.SysFont('Arial', 20).render("{} Unique Letters".format(self.numberOfLetters), True, (0,0,0)), (500,420))
			else:
				pygame.draw.rect(self.win, self.backgroundColor, (500,420,200,250))
			
			self.drawCircles()
			self.drawWord(word)
			pygame.display.update()


