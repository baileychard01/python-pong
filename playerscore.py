import pygame


class playerscore:

	def __init__(self):
		self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
		self.pscore = self.myfont.render("o", False, (0, 0, 0))

	def draw(self, screen):
		screen.blit(self.pscore,(462,50))
