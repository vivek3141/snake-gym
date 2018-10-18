import pygame
import sys
import time
import random
from snake_gym.envs.modules import *
from pygame.locals import *
import numpy as np


class SnakeGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        self.surface.fill((255, 255, 255))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.done = False

        pygame.key.set_repeat(1, 40)

        self.screen.blit(self.surface, (0, 0))
        pygame.init()
        self.fpsClock = pygame.time.Clock()

        self.snake = Snake()
        self.apple = Apple()

    def reset(self):
        return SnakeGame._get_image(self.surface)

    def step(self, key):
        length = self.snake.length
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                self.done = True

        act = [UP, DOWN, LEFT, RIGHT]
        self.snake.point(act[key])
        self.surface.fill((255, 255, 255))
        try:
            self.snake.move()
        except SnakeException:
            self.done = True
        if self.done:
            state = SnakeGame._get_image(self.surface)
            return state, length, self.done, {}
        check_eat(self.snake, self.apple)
        self.snake.draw(self.surface)
        self.apple.draw(self.surface)
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.snake.length), 1, (10, 10, 10))
        text_pos = text.get_rect()
        text_pos.centerx = 20
        self.surface.blit(text, text_pos)
        self.screen.blit(self.surface, (0, 0))
        state = SnakeGame._get_image(self.surface)
        pygame.display.flip()
        pygame.display.update()
        self.fpsClock.tick(self.fps + self.snake.length / 3)
        return state, self.snake.length, False, {}

    @staticmethod
    def _get_image(surface):
        ret = list(map(lambda x: list(x), np.zeros((SCREEN_HEIGHT, SCREEN_WIDTH))))
        for j in range(SCREEN_HEIGHT):
            for k in range(SCREEN_WIDTH):
                ret[j][k] = surface.get_at((k, j))
        return np.array(ret)
