import pygame
import sys
import time
import random
from snake_gym.envs.modules import *
from pygame.locals import *


class SnakeGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        self.surface.fill((255, 255, 255))
        self.clock = pygame.time.Clock()

        pygame.key.set_repeat(1, 40)

        self.screen.blit(self.surface, (0, 0))
        pygame.init()
        self.fpsClock = pygame.time.Clock()

        self.snake = Snake()
        self.apple = Apple()

    def step(self, key):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        act = [UP, DOWN, LEFT, RIGHT]
        self.snake.point(act[key])

        self.surface.fill((255, 255, 255))
        self.snake.move()
        check_eat(self.snake, self.apple)
        self.snake.draw(self.surface)
        self.apple.draw(self.surface)
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.snake.length), 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = 20
        #self.surface.blit(text, textpos)
        self.screen.blit(self.surface, (0, 0))
        print(self.surface)
        pygame.display.flip()
        pygame.display.update()
        self.fpsClock.tick(FPS + self.snake.length / 3)
        done = False
        return _, self.snake.length, done, {}


s = SnakeGame()
for i in range(100000):
    s.step(random.randint(0, 3))
