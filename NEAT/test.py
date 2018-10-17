import gym, snake_gym
import random

env = gym.make("snake-tiled.v0")
state = env.reset()
done = False
while not done:
    s, r, done, _ = env.step(random.randint(0, 3))
