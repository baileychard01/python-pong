import pygame
ballimage = pygame.image.load("Ball.png")

class ball:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.xvelocity = 1
		self.yvelocity = 1
		self.startx = x
		self.starty = y

	def draw(self,screen):
		screen.blit(ballimage, (self.x, self.y))

	def update(self):
		self.y += self.yvelocity
		self.x += self.xvelocity
		if self.y >= 256 - 5:
			self.yvelocity = -self.yvelocity
		if self.y <= 0:
			self.yvelocity = -self.yvelocity
		if self.x >= 512 - 6 or self.x <= 0:
			self.x = self.startx
			self.y = self.starty

	def bounce(self):
		self.xvelocity = -self.xvelocity


	def iscolliding(self,paddle):
		if self.x >= paddle.x and self.x <= paddle.x + 2:
			if self.y >= paddle.y and self.y <= paddle.y + 28:
				self.bounce()
				if paddle.x < 100:
					self.x = paddle.x + 2
				else:
					self.x = paddle.x - 6















