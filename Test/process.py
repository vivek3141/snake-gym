import snake_gym
import gym
from PIL import Image
import numpy as np
from snake_gym.envs.modules import *

GRID_HEIGHT = int(GRID_HEIGHT)
GRID_WIDTH = int(GRID_WIDTH)


def equals(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True


def process(img):
    ret = list(map(list, np.zeros((GRID_HEIGHT, GRID_WIDTH))))
    ret = list(map(lambda x: list(map(int, x)), ret))
    for i in range(0, SCREEN_HEIGHT, GRIDSIZE):
        for k in range(0, SCREEN_WIDTH, GRIDSIZE):
            if equals(img[i][k], [255, 0, 0, 255]):
                ret[int(i/15)][int(k/15)] = 1
            elif equals(img[i][k], [0, 0, 0, 255]):
                ret[int(i/15)][int(k/15)] = 2
        print(ret[int(i/15)])
    return ret


env = gym.make("snake-v0")
state, r, d, inf = env.step(1)
process(state)
im = Image.fromarray(state, 'RGBA')
im.show()
