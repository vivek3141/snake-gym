import gym
from gym import error, spaces, utils
from gym.utils import seeding
from snake_gym.envs.snake import SnakeGame


class SnakeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.observation_space = spaces.Box(low=0, high=3, shape=[150, 150])
        self._action_set = [x for x in range(4)]
        self.action_space = spaces.Discrete(4)
        self._s = SnakeGame()

    def step(self, action):
        state, reward, done, info = self._s.step(action)
        return state, reward, done, info

    def reset(self):
        self._s = SnakeGame()
        return self._s.reset()

    def render(self, mode='human', close=False):
        raise NotImplementedError
