import pygame
import pickle
from pygame.locals import *
import numpy as np

trainSize = 28
magnification = 20
canvasSize = trainSize*magnification
stroke = 30


pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 100)
screen = pygame.display.set_mode((canvasSize,canvasSize))
black = (0,0,0)
white = (255,255,255)

fileName = 'netCrossEntropy.pickle'
file = open(fileName,'rb')
net = pickle.load(file)


def getTrainSizeImage(screen):
	image = np.zeros((trainSize,trainSize))
	for y in range(trainSize):
		for x in range(trainSize):
			sum = 0
			for j in range(magnification):
				for i in range(magnification):
					sum+=screen.get_at((x*magnification+i, y*magnification))[0]*1.0
			average = sum/(magnification*magnification)
			image[y,x] = average
	return image

def turnToVec(screen):
	vec = np.zeros((trainSize*trainSize,1))
	image = getTrainSizeImage(screen)
	for i in range(trainSize):
		for j in range(trainSize):
			vec[i*trainSize+j] = image[i,j]/256
	return vec

def answer(screen, net):
	x = turnToVec(screen)
	a = net.forward(x)
	return np.argmax(a)


gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c:
				screen.fill(black)
			if event.key == pygame.K_t:
				#action
				a = answer(screen, net)
				textSurface = myfont.render(str(a), True, white)
				screen.blit(textSurface,(0,0))
	if pygame.mouse.get_pressed()[0]:
		mousePos = pygame.mouse.get_pos()
		pygame.draw.ellipse(screen, white, [mousePos[0], mousePos[1], stroke, stroke])

	pygame.display.update()

pygame.quit()
file.close()