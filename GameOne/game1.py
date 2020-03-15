from random import randint
import pgzrun
# from pgzero.actor import Actor
# from pgzero import keyboard, screen

WIDTH = 700
HEIGHT = 800
car = Actor("racecar")
car.pos = 250, 700
SPEED = 4
trackCount = 0
trackPosition = 250
trackWidth = 120
trackDirection = False
trackLeft = []
trackRight = []
gameStatus = 0

def draw():
	global gameStatus
	screen.fill((128, 128, 128))
	if gameStatus == 0:
		car.draw()
		b = 0
		while b < len(trackLeft):
			trackLeft[b].draw()
			trackRight[b].draw()
			b += 1
	if gameStatus == 1:
		screen.blit('rflag', (318, 268))
	if gameStatus == 2:
		screen.blit('cflag', (318, 268))

def update():
	global gameStatus, trackCount
	if gameStatus == 0:
		if keyboard.left: 
			car.x -= 2
		if keyboard.right:
			car.x += 2
		updateTrack()
	if trackCount > 200:
		gameStatus = 2

def makeTrack():
	global trackCount, trackLeft, trackRight, trackPosition, trackWidth
	trackLeft.append(Actor("barrier", pos = (trackPosition-trackWidth, 0)))
	trackRight.append(Actor("barrier", pos = (trackPosition+trackWidth, 0)))
	trackCount += 1

def updateTrack():
	global trackCount, trackPosition, trackDirection, trackWidth, gameStatus
	b = 0
	while b < len(trackLeft):
		if car.colliderect(trackLeft[b]) or car.colliderect(trackRight[b]):
			gameStatus = 1
		trackLeft[b].y += SPEED
		trackRight[b].y += SPEED
		b += 1
	if trackLeft[len(trackLeft) - 1].y > 32:
		if trackDirection == False:
			trackPosition += 16
		if trackDirection == True:
			trackPosition -= 16
		if randint(0 ,4) == 1:
			trackDirection = not trackDirection
		if trackPosition > 700 - trackWidth:
			trackDirection = True
		if trackPosition < trackWidth:
			trackDirection = False
		makeTrack()

makeTrack()

pgzrun.go()