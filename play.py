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
		self.width = 700 # width of game window	
		self.height = 480 # height of game window
		self.letters = {'a':False, 'b':False, 'c':False, 'd':False, 'e':False, 'f':False, 'g':False, 'h':False, 'i':False, 
						'j':False, 'k':False, 'l':False, 'm':False, 'n':False, 'o':False, 'p':False, 'q':False, 'r':False, 
						's':False, 't':False, 'u':False, 'v':False, 'w':False, 'x':False, 'y':False, 'z':False  }
		#the dictionary above keeps track of all the letters which have been pressed by the user, False means not pressed
		
		self.backgroundColor = (197, 227, 236) #blue
		self.circleColor = (199, 66, 97) #pink
		self.fontColor = (0,0,0) #black

		self.win = pygame.display.set_mode((self.width, self.height)) #creating the game window
		self.font = pygame.font.SysFont('comicsans', 30) # saving this font style

		self.hangman = 0 # number of incorrect entries by user
		self.wordLetterSet = set() # set of all the unique letters in the word
		self.numberOfLetters = 0 # number of unique letters (used for HINT) 
		self.gameFlag = True # flag which decides if the game is complete
		self.hintFlag = False # flag which tells wether or not to show the HINT
		self.words = words # self.words is the list of words, arg words is list of either easy,medium or hard words

		self.font_render = [] # will hold rendered fonts to save time while running
		for i in range(26):
			self.font_render.append(self.font.render(chr(i+65), 1, self.fontColor)) # adding all characters a-z

		self.image_render = [] # will hold render images to save time while running
		for i in range(1,8):
			self.image_render.append(pygame.image.load("Images/{}.png".format(i)))

		self.play() # calling the play function

	def initGame(self, word):
		for i in range(len(word)):
			pygame.draw.rect(self.win, (0,0,0), (50+i*30,440,15,2)) # drawing the rectabgles which look like empty spaces ('__')

		self.win.blit(self.image_render[0],(280,160)) # putting the image of hangman with no errors
		for i in word:
			self.wordLetterSet.add(i) # adding all the letter to the set
		self.numberOfLetters = len(self.wordLetterSet) # counting number of unique letters (for HINT)
		
	def renderScreen(self, text): #funtion is called when the game is over
		self.win.fill(self.backgroundColor) # removing all the elements
		fnt = pygame.font.SysFont("comicsans", 50) 
		if(text=="Win"): #if winner
			self.win.blit(fnt.render("You "+text, True, (27, 48, 28)), (290,300))
		else:
			self.win.blit(fnt.render("You "+text, True, (161,0,0)), (260,300))
		self.win.blit(self.image_render[6], (330, 220)) # image of the replay sign
		pygame.display.update()
		while True : #waiting for user input
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

	def drawCircles(self): # used to draw circles with alphabets
		for i in range(13):
			pygame.draw.circle(self.win, self.circleColor, (i*50+50,40), 20) #top 13 circles
			if(self.letters[chr(i+97)] == False): # only puts aplhabets on letters which are not pressed yet 
				self.win.blit(self.font_render[i], (i*50+43, 30))
			
			pygame.draw.circle(self.win, self.circleColor, (i*50+50,95), 20) # bottom 13 circles
			if(self.letters[chr(i+110)] == False): # only puts aplhabets on letters which are not pressed yet
				self.win.blit(self.font_render[i+13], (i*50+43, 85))

	def drawWord(self,word): # used to draw the letters in the word
		for i in range(len(word)):
			if(self.letters[word[i]]==True): # draws letter which are correctly guessed
				self.win.blit(self.font_render[ord(word[i])-97], (50+i*30,420))

	def letterPressed(self, letter, word):
		if(self.letters[letter] == True): # if letter already pressed earlier
			return True, True # return type is gameFlag, Result
		self.letters[letter] = True # if not pressed earlier then mark it as pressed now
		if(letter not in word): # if wrong letter
			self.hangman += 1 #mark as error
			os.system('mpg123 -q --no-control '+"Audio/invalid.mp3") # play inavalid sound
			pygame.draw.rect(self.win, self.backgroundColor, (280,160,200,250)) # cover the old hangman photo
			self.win.blit(self.image_render[self.hangman],(280,160)) # render new hangman photo
			if(self.hangman == 5): # if 5 errors recorded
				return False, False	# return type gameFlag, Result
		else: # correct letter
			os.system('mpg123 -q --no-control '+"Audio/valid.mp3") #play valid sound
			self.wordLetterSet.remove(letter) # remove letter from remaining letters
			if(len(self.wordLetterSet)==0): # if no letters remaining (all letters guessed correctly)
				return False, True # return type gameFlag, Result
		return True, True # for all other conditions, gameFlag, Result

	def play(self):
		self.win.fill(self.backgroundColor) #color the background
		word = random.choice(self.words) # choose a word at random
		print("The word is : " + str(word)) # print on the console
		self.initGame(word) 
		pygame.display.set_caption("Hangman")
		while(self.gameFlag):
			for event in pygame.event.get(): # wait for user input
					#quit game if user clicks the cross or pressed <esc>
					if(event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE)):
						pygame.quit()
						sys.exit()
					elif(event.type == KEYDOWN): 
						if(event.key == K_a):
							self.gameFlag,res = self.letterPressed('a', word)
						elif(event.key == K_b):
							self.gameFlag,res = self.letterPressed('b', word)
						elif(event.key == K_c):
							self.gameFlag,res = self.letterPressed('c', word)
						elif(event.key == K_d):
							self.gameFlag,res = self.letterPressed('d', word)
						elif(event.key == K_e):
							self.gameFlag,res = self.letterPressed('e', word)
						elif(event.key == K_f):
							self.gameFlag,res = self.letterPressed('f', word)
						elif(event.key == K_g):
							self.gameFlag,res = self.letterPressed('g', word)
						elif(event.key == K_h):
							self.gameFlag,res = self.letterPressed('h', word)
						elif(event.key == K_i):
							self.gameFlag,res = self.letterPressed('i', word)
						elif(event.key == K_j):
							self.gameFlag,res = self.letterPressed('j', word)
						elif(event.key == K_k):
							self.gameFlag,res = self.letterPressed('k', word)
						elif(event.key == K_l):
							self.gameFlag,res = self.letterPressed('l', word)
						elif(event.key == K_m):
							self.gameFlag,res = self.letterPressed('m', word)
						elif(event.key == K_n):
							self.gameFlag,res = self.letterPressed('n', word)
						elif(event.key == K_o):
							self.gameFlag,res = self.letterPressed('o', word)
						elif(event.key == K_p):
							self.gameFlag,res = self.letterPressed('p', word)
						elif(event.key == K_q):
							self.gameFlag,res = self.letterPressed('q', word)
						elif(event.key == K_r):
							self.gameFlag,res = self.letterPressed('r', word)
						elif(event.key == K_s):
							self.gameFlag,res = self.letterPressed('s', word)
						elif(event.key == K_t):
							self.gameFlag,res = self.letterPressed('t', word)
						elif(event.key == K_u):
							self.gameFlag,res = self.letterPressed('u', word)
						elif(event.key == K_v):
							self.gameFlag,res = self.letterPressed('v', word)
						elif(event.key == K_w):
							self.gameFlag,res = self.letterPressed('w', word)
						elif(event.key == K_x):
							self.gameFlag,res = self.letterPressed('x', word)
						elif(event.key == K_y):
							self.gameFlag,res = self.letterPressed('y', word)
						elif(event.key == K_z):
							self.gameFlag,res = self.letterPressed('z', word)
						elif(event.key == K_RETURN):
							self.hintFlag = not self.hintFlag
						
			if(self.hintFlag==True): # show hint
				self.win.blit(pygame.font.SysFont('Arial', 20).render("{} Unique Letters".format(self.numberOfLetters), True, (0,0,0)), (500,420))
			else: # cover with rectangle
				pygame.draw.rect(self.win, self.backgroundColor, (500,420,200,250))
			
			self.drawCircles()
			self.drawWord(word)
			pygame.display.update() # update the display screen
			if(self.gameFlag == False): # if game is finished
				if(res == True): # if player won
					os.system('mpg123 -q --no-control '+"Audio/win.mp3")		
					self.renderScreen("Win")
				else: # if player lost
					os.system('mpg123 -q --no-control '+"Audio/loose.mp3")		
					self.renderScreen("Loose")


