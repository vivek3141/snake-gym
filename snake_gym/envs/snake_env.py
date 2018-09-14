import gym
from gym import error, spaces, utils
from gym.utils import seeding
from snake_gym.envs.snake import SnakeGame


class SnakeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self._s = SnakeGame()

    def step(self, action):
        state, reward, done, info = self._s.step(action)
        return state, reward, done, info

    def reset(self):
        self._s = SnakeGame()

    def render(self, mode='human', close=False):
        raise NotImplementedError
