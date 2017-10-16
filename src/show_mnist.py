import pygame
import ImageDealer
import mnist_loader
import pickle
import numpy as np
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()


trainSize = 28
magnification = 20
canvasSize = trainSize*magnification


fileName = "net.pickle"
file = open(fileName, 'rb')
net = pickle.load(file)
file.close()
pygame.init()
screen = pygame.display.set_mode((canvasSize,canvasSize))

myfont = pygame.font.SysFont('Comic Sans MS', 100)
screen = pygame.display.set_mode((canvasSize,canvasSize))

white = (255,255,255)
def vecToArrayImage(vec):
	array = []
	for i in range(trainSize):
		array.append([])
		for j in range(trainSize):
			array[i].append(vec[i*trainSize+j][0])
	return array

gameExit = False
counter=0
while not gameExit:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				data = test_data[counter]
				inArray = vecToArrayImage(data[0])
				ImageDealer.displayImage(inArray, screen, magnification)
				a = np.argmax(net.forward(data[0]))
				textSurface = myfont.render(str(a), True, white)
				screen.blit(textSurface,(0,0))
				counter+=1
	pygame.display.update()
pygame.quit()