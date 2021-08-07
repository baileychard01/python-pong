import pygame

class playerbrain:
	def __init__ (self,upkey,downkey):
		self.upkey = upkey
		self.downkey = downkey
		self.movementDirection = 0

	def update(self,paddle,events,ball):
		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == self.downkey:
					self.movementDirection = 1
				if event.key == self.upkey:
					self.movementDirection = -1
			if event.type == pygame.KEYUP:
				if event.key == self.downkey:
					self.movementDirection = 0
				if event.key == self.upkey:
					self.movementDirection = 0
		paddle.y += self.movementDirection
		if paddle.y < 0:
			paddle.y=0
		if paddle.y > 256 -28:
			paddle.y = 256-28