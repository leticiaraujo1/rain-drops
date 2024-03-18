import pygame 
import random

class RainDrops(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y, size_x, size_y, speed):
		super().__init__()
		self.image = pygame.Surface((size_x, size_y))
		self.image.fill((54, 125, 201)) 
		self.rect = self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y
		self.speed = speed

	def update(self):
		self.rect.y += self.speed
		if self.rect.y >= 350:
			self.rect.y = 0

def main():
	pygame.init()

	width = 500
	height = 350
	screen = pygame.display.set_mode((width,height))

	clock = pygame.time.Clock()
	rain_sound = 'rain.wav'

	rain_drops = pygame.sprite.Group()

	for i in range(500):
		rain_drops.add(RainDrops(random.randint(0, width), random.randint(0, height), 2, 8, 5))

	pygame.mixer.music.load(rain_sound)
	pygame.mixer.music.play(-1)

	run = True
	while run: 
		
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				run = False
		
		rain_drops.update()

		screen.fill((0, 0, 0))
		rain_drops.draw(screen)
		
		pygame.display.flip()
		clock.tick(60)

if __name__ == "__main__":
    main()



