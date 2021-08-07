import pygame
paddleimage = pygame.image.load("Paddle.png")

class paddle:
	def __init__(self,x,y,brain):
		self.x = x
		self.y = y
		self.brain = brain

	def draw(self,screen):
		screen.blit(paddleimage, (self.x, self.y))

	def update(self,ball,events):
		self.brain.update(self,events,ball)
		ball.iscolliding(self)






