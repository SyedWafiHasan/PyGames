import pgzrun
from random import randint
import math
from pgzero import screen
from pgzero.actor import Actor

WIDTH = 800
HEIGHT = 600
LOOPDELAY = 80

myButtons = []

myButtons.append(Actor('redunlit',bottomright = (400,270)))
myButtons[0].state = False

myButtons.append(Actor('greenunlit',bottomleft = (400,270)))
myButtons[1].state = False

myButtons.append(Actor('blueunlit',topright = (400,270)))
myButtons[2].state = False

myButtons.append(Actor('yellowunlit',topleft = (400,270)))
myButtons[3].state = False

buttonsLit = ['redlit', 'greenlit', 'bluelit', 'yellowlit']
buttonsUnLit = ['redunlit', 'greenunlit', 'blueunlit', 'yellowunlit']

playButton = Actor('play', pos = (400, 540))
buttonList = []
playPosition = 0
playingAnimation = False
gameCountdown = -1
score = 0
playerInput = []
signalScore = False
gameStarted = False

def draw():
	global playingAnimation, score
	screen.fill((30, 10, 30))
	for b in myButtons:
		b.draw()
	if gameStarted:
		screen.draw.text("Score : "+str(score), (310, 540), owidth = 0.5, ocolor = (255, 255, 255), color = (255, 128, 0), fontsize = 60)
	else:
		playButton.draw()
		screen.draw.text("Play", (370, 525), owidth = 0.5, ocolor = (255, 255, 255), color = (255, 128, 0), fontsize = 40)
		if score > 0:
			screen.draw.text("Final Score : "+str(score), (250, 20), owidth = 0.5, ocolor = (255, 255, 255), color = (255, 128, 0), fontsize = 60)
		else:
			screen.draw.text("Press Play To Start", (220, 20), owidth = 0.5, ocolor = (255, 255, 255), color = (255, 128, 0), fontsize = 60)
	if playingAnimation or gameCountdown > 0:
		screen.draw.text("Watch", (330, 20), owidth = 0.5, ocolor = (255, 255, 255), color = (255, 128, 0), fontsize = 60)
	if not playingAnimation or gameCountdown == 0:
		screen.draw.text("Your Turn", (310, 20), owidth = 0.5, ocolor = (255, 255, 255), color = (255, 128, 0), fontsize = 60)
	
	playButton.draw()

def update():
	global myButtons, playingAnimation, playPosition, gameCountdown
	if playingAnimation:
		playPosition += 1
		listpos = math.floor(playPosition / LOOPDELAY)
		if listpos == len(buttonList):
			playingAnimation = False
			clearButtons()
		else:
			litButton = buttonList[listpos]
			if playPosition % LOOPDELAY > LOOPDELAY / 2:

def on_mouse_down(pos):
	global myButtons
	for b in myButtons:
		if b.collidepoint(pos):
			b.state = True

def on_mouse_up(pos):
	global myButtons
	for b in myButtons:
		b.state = False

def playAnimation():
	global playPosition, playingAnimation

pgzrun.go()