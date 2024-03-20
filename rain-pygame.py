import pygame 
import random

class RainDrops(pygame.sprite.Sprite):
	def __init__(self, width, height, size_x, size_y):
		super().__init__()
		self.image = pygame.Surface((size_x, size_y))
		self.image.fill((54, 125, 201))
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0, width)
		self.rect.y = random.randint(0, height)
		self.speed = random.uniform(3,5)

	def update(self):
		self.rect.y += self.speed
		self.rect.x += 1.2
		if self.rect.y >= 400:
			self.rect.y = 0
		if self.rect.x >= 600:
			self.rect.x = 0

def main():
	pygame.init()

	width = 600
	height = 400
	screen = pygame.display.set_mode((width,height))

	clock = pygame.time.Clock()
	rain_sound = 'rain.wav'

	raindrops = pygame.sprite.Group()

	for i in range(600):
		raindrops.add(RainDrops(width, height, 2, 8))

	pygame.mixer.music.load(rain_sound)
	pygame.mixer.music.play(-1)

	run = True
	while run: 
		
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				run = False
		
		raindrops.update()

		screen.fill((0, 0, 0))
		raindrops.draw(screen)
		
		pygame.display.flip()
		clock.tick(60)

if __name__ == "__main__":
    main()