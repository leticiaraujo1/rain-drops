import pygame 
import random

pygame.init() 

width = 500
height = 350
surface = pygame.display.set_mode((width,height))

blue = (0,0,255)

x = random.randint(0, width)

rain_sound = 'teste.mp3'


rain = pygame.draw.rect(surface, blue, pygame.Rect(x, 0, 4, 4))
pygame.display.flip()


pygame.mixer.music.load(rain_sound)
pygame.mixer.music.play(-1)

run = True
 
while run: 
	
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			run = False