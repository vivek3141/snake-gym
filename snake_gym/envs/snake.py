import pygame
import sys
import time
import random
from .modules import *
from pygame.locals import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((255, 255, 255))
clock = pygame.time.Clock()

pygame.key.set_repeat(1, 40)

screen.blit(surface, (0, 0))
pygame.init()
fpsClock = pygame.time.Clock()

snake = Snake()
apple = Apple()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            act = {K_UP: UP, K_DOWN: DOWN, K_LEFT:LEFT, K_RIGHT: RIGHT}
            try:
                snake.point(act[event.key])
            except KeyError:
                pass

    surface.fill((255, 255, 255))
    snake.move()
    check_eat(snake, apple)
    snake.draw(surface)
    apple.draw(surface)
    font = pygame.font.Font(None, 36)
    text = font.render(str(snake.length), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = 20
    surface.blit(text, textpos)
    screen.blit(surface, (0, 0))

    pygame.display.flip()
    pygame.display.update()
    fpsClock.tick(FPS + snake.length / 3)
