import gym
from gym import error, spaces, utils
from gym.utils import seeding
from snake_gym.envs.modules import *
from snake_gym.envs.snake_env import SnakeEnv
import numpy as np
from gym import spaces


class SnakeEnvTiled(SnakeEnv):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super().__init__()
        self.observation_space = spaces.Box(low=0, high=3, shape=[10, 10])
        self._action_set = [x for x in range(4)]
        self.action_space = spaces.Discrete(4)

    def reset(self):
        img = super().reset()
        return SnakeEnvTiled._process(img)

    def step(self, action):
        state, reward, done, info = self._s.step(action)
        state = SnakeEnvTiled._process(state)
        return state, reward, done, info

    @staticmethod
    def _equals(arr1, arr2):
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True

    @staticmethod
    def _process(img):
        ret = list(map(list, np.zeros((int(GRID_HEIGHT), int(GRID_WIDTH)))))
        ret = list(map(lambda x: list(map(int, x)), ret))
        for i in range(0, SCREEN_HEIGHT, GRIDSIZE):
            for k in range(0, SCREEN_WIDTH, GRIDSIZE):
                if SnakeEnvTiled._equals(img[i][k], [255, 0, 0, 255]):
                    ret[int(i / 15)][int(k / 15)] = 2
                elif SnakeEnvTiled._equals(img[i][k], [0, 0, 0, 255]):
                    ret[int(i / 15)][int(k / 15)] = 1
        return np.array(ret)
