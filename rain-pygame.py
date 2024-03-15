import pygame 
import random

pygame.init() 

width = 500
height = 350
screen = pygame.display.set_mode((width,height)) 

blue = (0,0,255)

y = 0

clock = pygame.time.Clock()

rain_sound = 'rain.wav'

class RainDrops:
	def __init__(self, surface, color, x, y):
		self.surface = surface
		self.color = color
		self.x = x
		self.y = y
		self.sizeX = 2
		self.sizeY = 10
		self.type = 'rect'
		self.create_Object()
	
	def create_Object(self):
		if self.type == 'rect':
			self.draw() 

	def draw(self):
		return pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.sizeX, self.sizeY))

	def fall():
		return True

for i in range(60):
	RainDrops(screen, blue, random.randint(0, width), y)
	

pygame.display.flip()


pygame.mixer.music.load(rain_sound)
pygame.mixer.music.play(-1)

run = True
 
while run: 
	
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			run = False

