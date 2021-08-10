import pygame


class aiscore:

	def __init__(self):
		self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
		self.score = self.myfont.render("o", False, (0, 0, 0))

	def draw(self, screen, ball):
		screen.blit(self.score,(50,50))


