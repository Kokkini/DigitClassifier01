import pygame

def shrink(inArray, factor):
	inH = len(inArray)
	inW = len(inArray[0])
	outH = inH/factor
	outW = inW/factor
	outArray = []
	for y in range(outH):
		outArray.append([])
		for x in range(outW):
			sum = 0
			for j in range(factor):
				for i in range(factor):
					sum += inArray[y*factor + j][x*factor + i]*1.0
			average = sum/(factor*factor)
		outArray[y].append(average)
	return outArray

def displayImage(inArray, screen, factor):
	inH = len(inArray)
	inW = len(inArray[0])
	
	for x in range(inW):
		for y in range(inH):
			color = int(inArray[y][x]*256)
			pygame.draw.rect(screen, (color, color, color), (x*factor,y*factor,factor,factor))




