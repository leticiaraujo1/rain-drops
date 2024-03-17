import pygame 
import random

class RainDrops():
	def __init__(self, surface, color, start_x, start_y):
		self.surface = surface
		self.color = color
		self.x = start_x
		self.y = start_y
		self.sy = start_y
		self.sizeX = 2
		self.sizeY = 10
		self.type = 'rect'

	def draw(self):
		return pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.sizeX, self.sizeY))

	def fall(self):
		if self.y == 350:
			self.y = self.sy
		else:
			self.y += 1

def main():
	pygame.init()

	width = 500
	height = 350
	screen = pygame.display.set_mode((width,height))

	blue = (0,0,255) 
	y = 0
	clock = pygame.time.Clock()
	rain_sound = 'rain.wav'

	rain_drops = []
	for i in range(60):
		rain_drops.append(RainDrops(screen, blue, random.randint(0, width), y))

	pygame.mixer.music.load(rain_sound)
	pygame.mixer.music.play(-1)

	run = True
	while run: 
		
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				run = False
		
		for rect in rain_drops:
			rect.fall()
		
		pygame.display.flip()
		clock.tick(60)

if __name__ == "__main__":
    main()




