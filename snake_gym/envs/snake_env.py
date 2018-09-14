import gym
from gym import error, spaces, utils
from gym.utils import seeding
from snake_gym.envs.snake import Snake

class SnakeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self._s = Snake()

    def step(self, action):
        self._s.step(action)

    def reset(self):
        self._s = Snake()

    def render(self, mode='human', close=False):
        raise NotImplementedError
