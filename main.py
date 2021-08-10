import pygame
from paddle import paddle
from aibrain import aibrain
from ball import ball
from aiscore import aiscore
from playerscore import playerscore
from playerbrain import playerbrain
pygame.font.init()


running = True
background = pygame.image.load("Background.png")
screen = pygame.display.set_mode([512, 256])

playerpaddle = paddle(10,256/2-14,playerbrain(pygame.K_w,pygame.K_s))
aipaddle = paddle(512-10-2,256/2-14,aibrain())
ball = ball(253, 126)
aiscore = aiscore()
playerscore = playerscore()

while running:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			running = False
	if not running:
		break
	playerpaddle.update(ball,events)
	aipaddle.update(ball,events)
	ball.update()
	pygame.display.flip()
	screen.blit(background, (0,0))
	ball.draw(screen)
	playerpaddle.draw(screen)
	aipaddle.draw(screen)
	aiscore.draw(screen)
	playerscore.draw(screen)

pygame.init()
pygame.font.init()
