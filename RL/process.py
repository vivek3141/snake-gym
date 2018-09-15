import snake_gym
import gym
from PIL import Image
import numpy as np
from snake_gym.envs.modules import *


def equals(arr1, arr2):
    for i in range(4):
        if arr1[i] != arr2[i]:
            return False
    return True


def process(img):
    ret = list(map(list, np.zeros((15, 15))))
    ret = list(map(lambda x: list(map(int, x)), ret))
    for i in range(GRID_HEIGHT):
        for k in range(GRID_WIDTH):
            if not equals(state[GRIDSIZE * i][GRIDSIZE * i], [255, 255, 255, 255]):
                ret[k][i] = 1
        print(ret[i])
    return ret


env = gym.make("snake-v0")
state, r, d, inf = env.step(1)
process(state)
im = Image.fromarray(state, 'RGBA')
im.show()
